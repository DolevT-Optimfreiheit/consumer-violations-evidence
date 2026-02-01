# WhatsApp chat parser
import re

def parse_whatsapp_chat(file_path):
    """Parse WhatsApp chat log into structured messages"""
    messages = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match WhatsApp message pattern
            pattern = r'(\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2}) - ([^:]+): (.+?)(?=\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2} -|$)'
            matches = re.findall(pattern, content, re.DOTALL)
            for match in matches:
                timestamp, sender, message = match
                is_me = 'Made in Market' not in sender and '÷×' in sender
                messages.append({
                    'timestamp': timestamp,
                    'sender': 'You' if is_me else 'Made in Market',
                    'message': message.strip(),
                    'is_me': is_me
                })
    except Exception as e:
        print(f"Error parsing chat: {e}")
    return messages

def highlight_legal_terms(text):
    """Highlight legal terms and violations in text"""
    legal_terms = [
        '§ 242 BGB', '§ 312j BGB', '§ 305c BGB', '§ 312a', '§ 5 UWG', '§ 433 BGB',
        'Verzug', 'default', 'breach', 'violation', 'illegal', 'void',
        'Specific Performance', 'Revolut', 'surcharge', 'discount'
    ]
    
    highlighted = text
    for term in legal_terms:
        if term in highlighted:
            highlighted = highlighted.replace(term, f'**{term}**')
    
    return highlighted
