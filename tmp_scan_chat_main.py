from pathlib import Path 
import re 
text = Path('WhatsApp Chat with Made in Market.txt').read_text(encoding='utf-8', errors='ignore') 
print('Total lines', len(text.splitlines())) 
print('Mentions of refund', text.lower().count('refund')) 
print('Mentions of cancel', text.lower().count('cancel')) 
print('Mentions of surcharge', text.lower().count('surcharge')) 
print('Mentions of shipping', text.lower().count('shipping')) 
print('Mentions of discount', text.lower().count('discount')) 
print('Mentions of default', text.lower().count('default')) 
print('Mentions of verzug', text.lower().count('verzug')) 
Path('tmp_chat_stats.txt').write_text(text[:2000], encoding='utf-8') 
