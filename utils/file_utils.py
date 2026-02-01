# File utility functions
from pathlib import Path

def get_image_base64(image_path):
    """Convert image to base64 for embedding"""
    import base64
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

def read_text_file(file_path):
    """Read text file content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def extract_pdf_text(pdf_path, max_pages=5):
    """Extract text from PDF file (first few pages for preview)"""
    try:
        import PyPDF2
        text_content = []
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = min(len(pdf_reader.pages), max_pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text.strip():
                    text_content.append(text)
        return "\n\n".join(text_content) if text_content else None
    except Exception as e:
        return None

def get_pdf_summary(pdf_path):
    """Get a brief summary from PDF (first 500 chars)"""
    text = extract_pdf_text(pdf_path, max_pages=2)
    if text:
        # Clean up text
        text = ' '.join(text.split())
        return text[:500] + "..." if len(text) > 500 else text
    return None
