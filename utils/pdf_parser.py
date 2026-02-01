# PDF Parser - Extract comprehensive information from PDFs
from pathlib import Path
import re
from datetime import datetime

def extract_full_pdf_text(pdf_path, max_pages=None):
    """Extract full text from PDF file"""
    try:
        import PyPDF2
        text_content = []
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages) if max_pages is None else min(len(pdf_reader.pages), max_pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text.strip():
                    text_content.append(text)
        return "\n\n".join(text_content) if text_content else None
    except Exception as e:
        return None

def parse_pdf_for_events(pdf_path):
    """Parse PDF to extract events, dates, amounts, and key information"""
    text = extract_full_pdf_text(pdf_path)
    if not text:
        return None
    
    events = []
    filename = Path(pdf_path).name
    
    # Extract dates from text (various formats)
    date_patterns = [
        r'(\d{1,2}[\s/.-]\d{1,2}[\s/.-]\d{2,4})',  # DD-MM-YYYY, DD/MM/YYYY, etc.
        r'(\d{4}[\s/.-]\d{1,2}[\s/.-]\d{1,2})',    # YYYY-MM-DD
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}',
        r'(\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})',
    ]
    
    # Extract order numbers
    order_patterns = [
        r'Order[#\s]*(\d+)',
        r'Order\s+Number[:\s]*(\d+)',
        r'#(\d{5,})',  # Order numbers typically 5+ digits
    ]
    
    # Extract amounts
    amount_patterns = [
        r'€\s*([\d,]+\.?\d*)',
        r'EUR\s*([\d,]+\.?\d*)',
        r'(\d+\.\d{2})\s*€',
        r'Total[:\s]*€?\s*([\d,]+\.?\d*)',
    ]
    
    # Extract key terms
    key_terms = {
        'surcharge': ['surcharge', 'additional charge', 'extra fee', 'post-payment'],
        'default': ['default_notice', 'verzug', 'breach', 'violation'],
        'rejection': ['rejection', 'refund rejected', 'denied'],
        'confirmation': ['confirmed', 'confirmation', 'order placed'],
        'payment': ['payment', 'paid', 'settlement', 'revolut'],
        'legal': ['legal notice', 'regulatory', 'BGB', 'UWG', 'violation'],
    }
    
    # Find dates
    dates_found = []
    for pattern in date_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            date_str = match.group(1) if match.groups() else match.group(0)
            dates_found.append(date_str)
    
    # Find order numbers
    order_numbers = []
    for pattern in order_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            order_numbers.append(match.group(1))
    
    # Find amounts
    amounts = []
    for pattern in amount_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            amount_str = match.group(1).replace(',', '')
            try:
                amounts.append(float(amount_str))
            except:
                pass
    
    # Detect key terms
    detected_terms = {}
    text_lower = text.lower()
    for term, keywords in key_terms.items():
        for keyword in keywords:
            if keyword in text_lower:
                detected_terms[term] = True
                break
    
    return {
        'filename': filename,
        'text': text,
        'dates': list(set(dates_found)),
        'order_numbers': list(set(order_numbers)),
        'amounts': list(set(amounts)),
        'key_terms': detected_terms,
        'full_text': text
    }

def analyze_all_pdfs(evidence_dir):
    """Analyze all PDF files in the evidence directory"""
    pdf_data = []
    evidence_path = Path(evidence_dir)
    
    for pdf_file in evidence_path.glob('*.pdf'):
        parsed = parse_pdf_for_events(pdf_file)
        if parsed:
            pdf_data.append(parsed)
    
    return pdf_data
