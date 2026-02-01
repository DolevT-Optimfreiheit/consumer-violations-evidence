import glob 
import PyPDF2 
from pathlib import Path 
out = [] 
files = glob.glob('*.pdf') 
files.sort() 
for name in files: 
    p = Path(name) 
    text = [] 
    with open(p,'rb') as f: 
        r = PyPDF2.PdfReader(f) 
        for page in r.pages: 
            t = page.extract_text() or '' 
            text.append(t) 
    out.append('FILE: ' + p.name) 
    out.append('\\n'.join(text)) 
Path('pdf_text_full.txt').write_text('\\n\\n'.join(out), encoding='utf-8') 
