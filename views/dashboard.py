# Dashboard page - High-performance legal layout
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from data.evidence_loader import get_all_evidence, format_file_size
from data.timeline_events import get_timeline_events
from utils.file_utils import get_pdf_summary

def render_dashboard_page():
    """Render the main dashboard page"""
    
    # Load evidence
    evidence = get_all_evidence()
    
    # Header Section
    st.markdown("# Case Dashboard")
    st.markdown("Complete overview of your legal case against Made in Market")
    st.write("")
    
    # Top Level Metrics
    total_files = sum(len(v) for v in evidence.values())
    
    timeline_events = get_timeline_events()
    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.metric("Evidence Files", total_files)
    with m2:
        st.metric("Legal Documents", len(evidence['legal']))
    with m3:
        st.metric("Legal Claims", "7")
    with m4:
        st.metric("Settlement Amount", "€473.85")
    with m5:
        st.metric("Key Events", len(timeline_events))
    
    st.write("")
    st.divider()
    
    # Main Content Grid
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("📂 Evidence Categories")
        with st.container(border=True):
            st.markdown(f"""
            ⚖️ **Legal Documents** — {len(evidence['legal'])} files  
            📦 **Order Confirmations** — {len(evidence['order'])} files  
            📸 **Photo Evidence** — {len(evidence['evidence'])} files  
            💬 **Communications** — {len(evidence['communication'])} logs  
            📄 **Other Documents** — {len(evidence['document'])} files
            """)
        
        st.write("")
        
        st.subheader("🎯 Case Overview")
        with st.container(border=True):
            st.markdown("""
            This case involves multiple contract and consumer protection violations:
            
            - **Product quality issues** with defective goods
            - **Hidden fees** added after checkout
            - **Pricing disputes** and unauthorized charges
            - **Service failures** and broken commitments
            
            All evidence has been documented and organized for legal proceedings.
            """)
        
        st.write("")
        
        st.subheader("🧭 Quick Navigation")
        with st.container(border=True):
            st.markdown("""
            **📅 Timeline** — See all events in chronological order  
            **📂 Evidence** — Browse and download all documents  
            **💬 Communications** — Review message history  
            **⚠️ Violations** — Detailed legal claims
            """)
    
    with col2:
        st.subheader("📋 Recent Activity")
        
        # Get recent files
        all_files = []
        for cat, files in evidence.items():
            for f in files:
                all_files.append({**f, 'category': cat})
        
        recent_files = sorted([f for f in all_files if f['date']], key=lambda x: x['date'], reverse=True)[:6]
        
        for item in recent_files:
            icon = item.get('icon', '📄')
            date_str = item['date'].strftime('%b %d, %Y') if item['date'] else 'Unknown date'
            
            with st.container(border=True):
                st.markdown(f"### {icon} {item['name']}")
                st.caption(f"📅 {date_str} • 📦 {item['category'].title()} • 💾 {format_file_size(item['size'])}")
                
                if item.get('description'):
                    st.markdown(f"_{item['description']}_")
                    st.write("")
                
                # Show preview for images, download button for PDFs
                if item['path'].exists():
                    file_ext = item['path'].suffix.lower()
                    if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
                        with st.expander("🖼️ View Image", expanded=False):
                            st.image(str(item['path']), use_container_width=True)
                    elif file_ext == '.pdf':
                        col_a, col_b = st.columns([1, 3])
                        with col_a:
                            with open(item['path'], 'rb') as f:
                                st.download_button(
                                    "📥 Download",
                                    f.read(),
                                    item['name'],
                                    mime="application/pdf",
                                    key=f"dash_dl_{item['name']}"
                                )
                        with col_b:
                            # Show PDF preview if available
                            pdf_summary = get_pdf_summary(item['path'])
                            if pdf_summary:
                                with st.expander("👁️ Preview Content"):
                                    st.text(pdf_summary[:500] + "..." if len(pdf_summary) > 500 else pdf_summary)
        
        st.write("")
        st.divider()
        st.subheader("🗓️ Latest Events")
        timeline_events = sorted(timeline_events, key=lambda x: x.get("date", ""), reverse=True)[:5]
        for event in timeline_events:
            with st.container(border=True):
                type_icon = {'order': '📦', 'legal': '⚖️', 'communication': '💬', 'incident': '⚡'}.get(event.get('type', ''), '📄')
                st.markdown(f"**{type_icon} {event.get('title', 'Untitled Event')}**")
                st.caption(f"📅 {event.get('date', 'Unknown date')}")
                summary = event.get("desc") or event.get("summary") or ""
                if summary:
                    summary = " ".join(summary.split())
                    st.write(summary[:120] + ("..." if len(summary) > 120 else ""))

if __name__ == "__main__":
    render_dashboard_page()
