# Evidence Browser View - Integrated Audit Repository
import streamlit as st
from pathlib import Path
import sys
from datetime import datetime

sys.path.append(str(Path(__file__).parent.parent))

from data.evidence_loader import get_all_evidence, format_file_size
from data.evidence_mapping import get_image_context, get_violations_for_image
from utils.file_utils import get_pdf_summary

def render_evidence_browser_page():
    """Render the evidence repository interface"""
    
    evidence = get_all_evidence()
    
    st.markdown("# 📂 Evidence Files")
    st.markdown("Browse and download all case documents and photos")
    st.write("")

    # Search and filters in collapsible section
    with st.expander("🔍 Search & Filter", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            search_text = st.text_input("Search files", placeholder="Enter filename or keyword...")
        with col2:
            sort_choice = st.selectbox("Sort by", ["Date (newest)", "Date (oldest)", "Name (A-Z)", "Size (largest)"])
        
        col3, col4, col5 = st.columns(3)
        with col3:
            type_filter = st.selectbox("File type", ["All", "PDF", "Images", "Text"])
        with col4:
            show_previews = st.checkbox("Show previews", value=False)
        with col5:
            only_with_violations = st.checkbox("Violations only", value=False)
    def match_item(item):
        if not search_text:
            return True
        hay = f"{item.get('name','')} {item.get('description','')} {item.get('relative_path','')}".lower()
        return search_text.lower() in hay
    
    st.write("")
    tabs = st.tabs([
        f"⚖️ Legal ({len(evidence['legal'])})",
        f"📦 Orders ({len(evidence['order'])})",
        f"📸 Photos ({len(evidence['evidence'])})",
        f"📄 All Files ({sum(len(v) for v in evidence.values())})"
    ])

    def passes_type_filter(item):
        if type_filter == "All":
            return True
        suffix = item.get("path").suffix.lower() if item.get("path") else ""
        if type_filter == "PDF":
            return suffix == ".pdf"
        if type_filter == "Images":
            return suffix in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]
        if type_filter == "Text":
            return suffix in [".txt", ".text"]
        return True

    def apply_sort(items):
        if sort_choice == "Date (newest)":
            return sorted(items, key=lambda x: x['date'] or datetime.min, reverse=True)
        if sort_choice == "Date (oldest)":
            return sorted(items, key=lambda x: x['date'] or datetime.min)
        if sort_choice == "Name (A–Z)":
            return sorted(items, key=lambda x: x.get('name', '').lower())
        if sort_choice == "Size (largest)":
            return sorted(items, key=lambda x: x.get('size', 0), reverse=True)
        return items
    
    def count_items(items):
        return len([i for i in items if match_item(i) and passes_type_filter(i)])

    # Legal Documents Tab
    with tabs[0]:
        legal_items = apply_sort([i for i in evidence['legal'] if match_item(i) and passes_type_filter(i)])
        st.markdown(f"**{len(legal_items)} legal documents**")
        if legal_items:
            export_text = "\n".join([f"{i['name']} | {i.get('description','')}" for i in legal_items])
            st.download_button("📥 Export List", export_text.encode("utf-8"), "legal_docs_list.txt", mime="text/plain")
        st.write("")
        for item in legal_items:
            if not match_item(item):
                continue
            date_str = item['date'].strftime('%b %d, %Y') if item['date'] else "Unknown"
            with st.container(border=True):
                st.markdown(f"### 📄 {item['name']}")
                st.caption(f"📅 {date_str} • 💾 {format_file_size(item['size'])}")
                
                if item.get('description'):
                    st.markdown(f"_{item['description']}_")
                
                # Actions row
                col_a, col_b = st.columns([1, 3])
                with col_a:
                    if item['path'].exists():
                        if item['path'].suffix.lower() == '.pdf':
                            with open(item['path'], 'rb') as f:
                                st.download_button(
                                    "📥 Download",
                                    f.read(),
                                    item['name'],
                                    mime="application/pdf",
                                    key=f"dl_l_{item['name']}"
                                )
                        else:
                            with open(item['path'], 'rb') as f:
                                st.download_button("📥 Download", f.read(), item['name'], key=f"dl_l_{item['name']}")
                
                with col_b:
                    # Show PDF preview text if available
                    if show_previews and item['path'].exists() and item['path'].suffix.lower() == '.pdf':
                        pdf_summary = get_pdf_summary(item['path'])
                        if pdf_summary:
                            with st.expander("👁️ Preview"):
                                st.text(pdf_summary[:500] + "..." if len(pdf_summary) > 500 else pdf_summary)
    
    # Orders Tab
    with tabs[1]:
        order_items = apply_sort([i for i in evidence['order'] if match_item(i) and passes_type_filter(i)])
        st.markdown(f"**{len(order_items)} order confirmations**")
        if order_items:
            export_text = "\n".join([f"{i['name']} | {i.get('description','')}" for i in order_items])
            st.download_button("📥 Export List", export_text.encode("utf-8"), "order_docs_list.txt", mime="text/plain")
        st.write("")
        for item in order_items:
            if not match_item(item):
                continue
            date_str = item['date'].strftime('%b %d, %Y') if item['date'] else "Unknown"
            with st.container(border=True):
                st.markdown(f"### 📦 {item['name']}")
                st.caption(f"📅 {date_str} • 💾 {format_file_size(item['size'])}")
                
                if item.get('description'):
                    st.markdown(f"_{item['description']}_")
                
                col_a, col_b = st.columns([1, 3])
                with col_a:
                    if item['path'].exists():
                        with open(item['path'], 'rb') as f:
                            st.download_button(
                                "📥 Download",
                                f.read(),
                                item['name'],
                                mime="application/pdf",
                                key=f"dl_o_{item['name']}"
                            )
                
                with col_b:
                    if show_previews and item['path'].exists():
                        pdf_summary = get_pdf_summary(item['path'])
                        if pdf_summary:
                            with st.expander("👁️ Preview"):
                                st.text(pdf_summary[:500] + "..." if len(pdf_summary) > 500 else pdf_summary)
    
    # Photographic Evidence
    with tabs[2]:
        photo_items = apply_sort([i for i in evidence['evidence'] if match_item(i) and passes_type_filter(i)])
        if only_with_violations:
            photo_items = [i for i in photo_items if get_violations_for_image(i['name'])]
        st.markdown(f"**{len(photo_items)} photos**")
        if photo_items:
            export_text = "\n".join([f"{i['name']} | {get_image_context(i['name']).get('description','')}" for i in photo_items])
            st.download_button("📥 Export List", export_text.encode("utf-8"), "photo_evidence_list.txt", mime="text/plain")
        st.write("")
        for item in photo_items:
            if not match_item(item):
                continue
            if only_with_violations and not get_violations_for_image(item['name']):
                continue
            image_info = get_image_context(item['name'])
            context = image_info.get('context', item['name'])
            
            with st.container(border=True):
                st.markdown(f"### 📸 {context}")
                
                if image_info.get('description'):
                    st.caption(image_info.get('description'))
                
                # Associated violations
                violations = get_violations_for_image(item['name'])
                if violations:
                    st.warning(f"⚠️ Related to: {', '.join(violations)}")
                
                if item['path'].exists():
                    if show_previews:
                        st.image(str(item['path']), use_container_width=True)
                    
                    # Download button
                    with open(item['path'], 'rb') as f:
                        st.download_button(
                            f"📥 Download",
                            f.read(),
                            item['name'],
                            key=f"dl_img_{item['name']}"
                        )
    
    # All Assets
    with tabs[3]:
        all_files = []
        for cat, files in evidence.items():
            for f in files: all_files.append({**f, 'category': cat})
        
        all_files = apply_sort([i for i in all_files if match_item(i) and passes_type_filter(i)])
        st.markdown(f"**{len(all_files)} total files**")
        if all_files:
            export_text = "\n".join([f"{i['name']} | {i.get('category','')} | {i.get('description','')}" for i in all_files])
            st.download_button("📥 Export List", export_text.encode("utf-8"), "all_files_list.txt", mime="text/plain")
        st.write("")
        for item in all_files:
            if not match_item(item):
                continue
            icon = item.get('icon', '📄')
            with st.container(border=True):
                c1, c2, c3 = st.columns([1, 8, 2])
                with c1: 
                    st.write(icon)
                with c2: 
                    st.write(f"**{item['name']}**")
                    st.caption(f"Category: {item['category']} • Size: {format_file_size(item['size'])}")
                    
                    # Display previews if enabled; downloads always available
                    if item['path'].exists() and show_previews:
                        file_ext = item['path'].suffix.lower()
                        if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
                            st.image(str(item['path']), caption=item['name'], use_container_width=True)
                        elif file_ext == '.pdf':
                            # Show PDF preview if available
                            pdf_summary = get_pdf_summary(item['path'])
                            if pdf_summary:
                                with st.expander(f"📄 Preview: {item['name']}"):
                                    st.text(pdf_summary)
                    if item['path'].exists():
                        file_ext = item['path'].suffix.lower()
                        if file_ext == '.pdf':
                            with open(item['path'], 'rb') as f:
                                st.download_button(
                                    "📄 Download PDF",
                                    f.read(),
                                    item['name'],
                                    mime="application/pdf",
                                    key=f"dl_all_{item['name']}"
                                )
                        elif file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
                            with open(item['path'], 'rb') as f:
                                st.download_button(
                                    "📥 Download Image",
                                    f.read(),
                                    item['name'],
                                    key=f"dl_all_img_{item['name']}"
                                )
                        else:
                            with open(item['path'], 'rb') as f:
                                st.download_button(
                                    "📥 Download File",
                                    f.read(),
                                    item['name'],
                                    key=f"dl_all_file_{item['name']}"
                                )
                with c3: 
                    st.caption(item['date'].strftime('%Y-%m-%d') if item['date'] else '---')

if __name__ == "__main__":
    render_evidence_browser_page()
