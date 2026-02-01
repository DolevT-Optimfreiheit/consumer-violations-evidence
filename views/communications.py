# Communications View - Streamlined Chat Interface
import streamlit as st
from pathlib import Path
import sys
from datetime import datetime
import re

sys.path.append(str(Path(__file__).parent.parent))

from utils.chat_parser import parse_whatsapp_chat, highlight_legal_terms
from data.evidence_loader import format_file_size, get_all_evidence

EVIDENCE_DIR = Path(__file__).parent.parent

def render_communications_page():
    """Render the communications audit log"""
    
    st.markdown("# 💬 Communications")
    st.markdown("WhatsApp message history with Made in Market")
    st.write("")
    
    # Load all evidence to get WhatsApp images dynamically
    all_evidence = get_all_evidence()
    
    # Load chat files
    main_chat = EVIDENCE_DIR / "WhatsApp Chat with Made in Market.txt"
    self_chat = EVIDENCE_DIR / "WhatsApp_Chat_Archive_Customer_Sent.txt"
    
    tabs = st.tabs(["💬 Main Chat", "📱 Notes"])
    
    with tabs[0]:
        if main_chat.exists():
            messages = parse_whatsapp_chat(main_chat)
            st.info(f"📊 {len(messages)} total messages in conversation")
            
            with st.expander("🔍 Filter Messages", expanded=False):
                col1, col2, col3 = st.columns(3)
                with col1:
                    show_me = st.checkbox("My messages only", value=False)
                    show_market = st.checkbox("Merchant messages only", value=False)
                
                with col2:
                    only_attachments = st.checkbox("Messages with files only", value=False)
                    only_legal = st.checkbox("Legal keywords only", value=False)
                
                with col3:
                    hide_empty = st.checkbox("Hide empty messages", value=True)
                    compact_mode = st.checkbox("Compact view", value=True)
                
                st.write("")
                search_text = st.text_input("Search", placeholder="Search message content...")
                
                col_d1, col_d2 = st.columns(2)
                with col_d1:
                    start_date = st.text_input("From date (YYYY-MM-DD)", value="")
                with col_d2:
                    end_date = st.text_input("To date (YYYY-MM-DD)", value="")
            
            st.write("")

            def parse_msg_date(ts):
                try:
                    return datetime.strptime(ts.split(' - ')[0], "%d/%m/%Y, %H:%M").date()
                except Exception:
                    return None

            def in_date_range(ts):
                msg_date = parse_msg_date(ts)
                if not msg_date:
                    return True
                if start_date:
                    try:
                        if msg_date < datetime.strptime(start_date, "%Y-%m-%d").date():
                            return False
                    except Exception:
                        pass
                if end_date:
                    try:
                        if msg_date > datetime.strptime(end_date, "%Y-%m-%d").date():
                            return False
                    except Exception:
                        pass
                return True
            
            st.write("")
            filtered_messages = []
            for msg in messages:
                if show_me and not msg["is_me"]:
                    continue
                if show_market and msg["is_me"]:
                    continue
                if search_text and search_text.lower() not in msg["message"].lower():
                    continue
                if not in_date_range(msg["timestamp"]):
                    continue
                if hide_empty and not msg["message"].strip():
                    continue
                if only_attachments and "file attached" not in msg["message"].lower():
                    continue
                if only_legal:
                    legal_terms = [
                        "§", "bgb", "uwg", "verzug", "default", "breach",
                        "violation", "illegal", "specific performance", "revolut",
                        "surcharge", "refund", "compensation"
                    ]
                    if not any(term in msg["message"].lower() for term in legal_terms):
                        continue
                filtered_messages.append(msg)

            st.markdown(f"**Showing {len(filtered_messages)} messages**")
            if filtered_messages:
                export_text = "\n".join([f"{m['timestamp']} - {m['sender']}: {m['message']}" for m in filtered_messages])
                st.download_button("📥 Export Messages", export_text.encode("utf-8"), "messages_export.txt", mime="text/plain")
            
            st.write("")
            for msg in filtered_messages:
                role = "user" if msg['is_me'] else "assistant"
                label = "You" if msg['is_me'] else "Made in Market"
                avatar = "👤" if msg['is_me'] else "🏪"
                
                with st.chat_message(role, avatar=avatar):
                    st.caption(f"**{label}** • {msg['timestamp']}")
                    message_text = msg['message']
                    if compact_mode and len(message_text) > 400:
                        st.markdown(highlight_legal_terms(message_text[:400] + "..."))
                        with st.expander("Read more"):
                            st.markdown(highlight_legal_terms(message_text))
                    else:
                        st.markdown(highlight_legal_terms(message_text))
            
            st.divider()
            
            # Show all WhatsApp images dynamically from evidence loader
            st.subheader("📸 Shared Images")
            
            # Get all WhatsApp images from evidence (all images with 'whatsapp' in name or IMG- pattern)
            whatsapp_images = []
            for item in all_evidence['evidence']:
                img_name = item['name']
                img_name_lower = img_name.lower()
                # Match WhatsApp Image *.jpeg files or IMG-*.jpg files (WhatsApp image pattern)
                if 'whatsapp' in img_name_lower or img_name.startswith('IMG-'):
                    whatsapp_images.append(item)
            
            # Sort by date (most recent first)
            whatsapp_images.sort(key=lambda x: x['date'] if x['date'] else datetime.min, reverse=True)
            
            if whatsapp_images:
                for item in whatsapp_images:
                    if item['path'].exists():
                        with st.container(border=True):
                            if item.get('description'):
                                st.markdown(f"**{item.get('description')}**")
                            st.image(str(item['path']), use_container_width=True)
                            st.caption(item['name'])
            else:
                st.info("No shared images found")
            
            st.divider()
            with open(main_chat, 'rb') as f:
                st.download_button("📥 Download Full Chat Log", f.read(), main_chat.name)
        else:
            st.error("Main Correspondence file not found.")

    with tabs[1]:
        if self_chat.exists():
            messages = parse_whatsapp_chat(self_chat)
            st.info(f"📊 {len(messages)} preserved notes and forwards")
            compact_notes = st.checkbox("Compact view", value=True, key="compact_notes")
            st.write("")
            
            for msg in messages:
                # Typically these are notes to self or context preserving forwards
                with st.chat_message("user", avatar="📝"):
                    st.caption(f"**Note** • {msg['timestamp']}")
                    message_text = msg['message']
                    if compact_notes and len(message_text) > 400:
                        st.markdown(highlight_legal_terms(message_text[:400] + "..."))
                        with st.expander("Read more"):
                            st.markdown(highlight_legal_terms(message_text))
                    else:
                        st.markdown(highlight_legal_terms(message_text))
            
            st.divider()
            with open(self_chat, 'rb') as f:
                st.download_button("📥 Download Notes Archive", f.read(), self_chat.name)
        else:
            st.warning("Supplementary log file not found.")

if __name__ == "__main__":
    render_communications_page()
