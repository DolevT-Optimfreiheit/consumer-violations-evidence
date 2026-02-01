# Evidence loader - scans and categorizes all files
from pathlib import Path
from datetime import datetime
import re

# Get evidence directory relative to this file
EVIDENCE_DIR = Path(__file__).parent.parent

def parse_date_from_filename(filename):
    """Extract date from filename if present"""
    patterns = [
        r'(\d{4}-\d{2}-\d{2})',  # 2025-11-19
        r'(\d{8})',              # 20251211
    ]
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            try:
                date_str = match.group(1)
                if '-' in date_str:
                    return datetime.strptime(date_str, '%Y-%m-%d')
                else:
                    return datetime.strptime(date_str, '%Y%m%d')
            except:
                pass
    return None

def get_file_category(filename):
    """Categorize files by type"""
    name_lower = filename.lower()
    
    # Skip app files
    if filename.endswith(('.py', '.txt')) and filename in ['app.py', 'requirements.txt']:
        return None, None
    
    if filename.endswith('.pdf'):
        if 'order' in name_lower and 'confirmed' in name_lower:
            return 'order', '📦'
        elif 'rejection' in name_lower or 'default' in name_lower or 'binding' in name_lower or 'empty_email' in name_lower:
            return 'legal', '⚖️'
        else:
            return 'legal', '⚖️'
    elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
        # All images go to evidence, including WhatsApp images
        return 'evidence', '📸'
    elif filename.endswith('.eml'):
        return 'communication', '💬'
    elif 'whatsapp' in name_lower and filename.endswith('.txt'):
        # Only WhatsApp text files go to communication
        return 'communication', '💬'
    elif 'default_notice' in name_lower or (filename.endswith('.txt') and 'whatsapp' not in name_lower and 'pdf_analysis' not in name_lower):
        return 'legal', '⚖️'
    else:
        return 'document', '📄'

def extract_order_number(filename):
    """Extract order number from filename if present"""
    import re
    match = re.search(r'Order[_\s]*#?(\d+)', filename, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def get_file_description(filename, category):
    """Generate a description based on filename and category"""
    name_lower = filename.lower()
    
    if category == 'order':
        order_num = extract_order_number(filename)
        if order_num:
            return f"Order confirmation for Order #{order_num}"
        return "Order confirmation document"
    
    elif category == 'legal':
        if 'default' in name_lower or 'verzug' in name_lower:
            return "Formal Declaration of Default (Verzug)"
        elif 'rejection' in name_lower:
            return "Rejection of Unilateral Refund - Notice of Regulatory Action"
        elif 'binding' in name_lower:
            return "Binding Confirmation - Reinstated Subscription Agreement"
        elif 'empty_email' in name_lower:
            return "Empty Email - WhatsApp Follow-up Documentation"
        return "Legal document"
    
    elif category == 'evidence':
        if '20251211' in filename:
            return "Product replacement specifications (Parmalat)"
        elif '20251219' in filename:
            return "Damaged/punctured packages evidence"
        elif '20251225' in filename:
            return "Rotten milk and contaminated product evidence (minority of delivery)"
        elif '2026-01-16' in filename:
            return "Order #16045 pricing and payment evidence"
        elif '2026-01-20' in filename:
            return "Terms of Service and Shipping Policy screenshots"
        elif '2026-01-21' in filename:
            return "Additional legal documentation"
        return "Photographic evidence"
    
    elif category == 'communication':
        if filename.endswith('.eml'):
            return "Email message"
        return "WhatsApp chat log"
    
    return "Document"

def get_all_evidence():
    """Get all evidence files organized by category - recursively scans all subdirectories"""
    evidence = {
        'legal': [],
        'order': [],
        'evidence': [],
        'communication': [],
        'document': []
    }
    
    # Skip these directories when scanning
    skip_dirs = {'__pycache__', '.git', 'node_modules', 'venv', '.venv', 'env'}
    
    if EVIDENCE_DIR.exists():
        # Recursively scan all files in directory and subdirectories
        for file_path in EVIDENCE_DIR.rglob('*'):
            # Skip directories and files in skip_dirs
            if file_path.is_file():
                # Check if file is in a skipped directory
                if any(skip_dir in file_path.parts for skip_dir in skip_dirs):
                    continue
                
                # Skip Python files in subdirectories (components/, views/, data/, utils/)
                if file_path.suffix == '.py' and file_path.parent != EVIDENCE_DIR:
                    continue
                
                category, icon = get_file_category(file_path.name)
                if category:  # Skip None categories (app files)
                    date = parse_date_from_filename(file_path.name)
                    description = get_file_description(file_path.name, category)
                    order_num = extract_order_number(file_path.name) if category == 'order' else None
                    
                    # Store relative path for display, but keep full path for access
                    relative_path = file_path.relative_to(EVIDENCE_DIR)
                    
                    evidence[category].append({
                        'name': file_path.name,
                        'path': file_path,  # Full path for file access
                        'relative_path': str(relative_path),  # Relative path for display
                        'size': file_path.stat().st_size,
                        'date': date,
                        'icon': icon,
                        'description': description,
                        'order_number': order_num
                    })
    
    # Sort each category by date
    for cat in evidence:
        evidence[cat].sort(key=lambda x: x['date'] or datetime.min, reverse=True)
    
    return evidence

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
