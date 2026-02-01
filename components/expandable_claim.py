# Professional Expandable Claim Component - Clean Minimal Design
import streamlit as st
from pathlib import Path
import sys
import hashlib

sys.path.append(str(Path(__file__).parent.parent))
from utils.file_utils import get_pdf_summary


def _stable_key_id(violation_key):
    """Stable short id for widget keys."""
    return hashlib.md5(violation_key.encode()).hexdigest()[:12]


def _evidence_key(claim_id, evidence):
    """Stable key per evidence item."""
    f = evidence.get("file") or evidence.get("context") or ""
    return f"{claim_id}_{hashlib.md5(str(f).encode()).hexdigest()[:10]}"


def _render_image_gallery(images, gallery_key, L):
    """Compact image gallery with minimal navigation."""
    if not images:
        return

    state_key = f"gallery_{gallery_key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    current_idx = st.session_state[state_key]
    total = len(images)
    current_idx = max(0, min(current_idx, total - 1))
    st.session_state[state_key] = current_idx

    img = images[current_idx]
    img_path = img["path"]
    context = img.get("context", "")
    description = img.get("description", "")
    filename = img.get("file", "")

    # Compact navigation row
    nav_col1, nav_col2, nav_col3 = st.columns([1, 3, 1])
    with nav_col1:
        if current_idx > 0:
            if st.button("◀", key=f"{gallery_key}_prev", help=L('previous', 'Previous')):
                st.session_state[state_key] = current_idx - 1
                st.rerun()
    with nav_col2:
        of_text = L('of', 'of')
        st.markdown(f"<p style='text-align:center;margin:0;color:#888;font-size:0.85rem;'><b>{current_idx + 1}</b> {of_text} {total}</p>", unsafe_allow_html=True)
    with nav_col3:
        if current_idx < total - 1:
            if st.button("▶", key=f"{gallery_key}_next", help=L('next', 'Next')):
                st.session_state[state_key] = current_idx + 1
                st.rerun()

    # Image
    if img_path.exists():
        st.image(str(img_path), use_container_width=True)
    else:
        add_file_text = L('add_file', 'Add file')
        st.caption(f"_{add_file_text}:_ `{filename}`")

    # Simple caption - context as title, description below
    if context or description:
        caption_text = f"**{context}**" if context else ""
        if description:
            caption_text += f"  \n{description}" if caption_text else description
        st.caption(caption_text)


def _render_documents_compact(documents, claim_id, evidence_dir, L):
    """Render documents as a compact list with expandable preview."""
    if not documents:
        return
    
    for idx, evidence in enumerate(documents):
        ek = _evidence_key(claim_id, evidence)
        doc_path = Path(evidence_dir) / evidence.get('file', '')
        context = evidence.get('context', 'Document')
        desc = evidence.get('description', '')
        
        file_data = b""
        preview_text = None
        preview_md = None
        
        if doc_path.exists():
            try:
                with open(doc_path, 'rb') as f:
                    file_data = f.read()
            except Exception:
                pass
            if doc_path.suffix.lower() == '.pdf':
                preview_text = get_pdf_summary(doc_path)
            elif doc_path.suffix.lower() == '.md':
                try:
                    preview_md = doc_path.read_text(encoding="utf-8")
                except Exception:
                    pass

        fn = evidence.get("file") or doc_path.name
        suffix = (fn or "").lower()
        mime = "application/pdf" if suffix.endswith(".pdf") else "text/markdown" if suffix.endswith(".md") else "application/octet-stream"

        # Compact: icon + name, with expander for preview
        with st.expander(f"📄 {context}", expanded=False):
            if desc:
                st.caption(desc)
            if preview_md:
                st.markdown(preview_md)
            elif preview_text:
                st.text(preview_text)
            elif file_data:
                st.caption(L('preview_not_available', 'Preview not available for this file type.'))
            else:
                st.caption(L('file_not_found', 'File not found.'))
            
            st.download_button(
                L('download', 'Download'),
                file_data or b"",
                fn,
                mime=mime,
                key=f"dl_doc_{ek}",
                disabled=not file_data,
            )


def _render_other_evidence_compact(evidence_list, claim_id, L):
    """Render chat/call evidence compactly."""
    if not evidence_list:
        return
    
    for idx, evidence in enumerate(evidence_list):
        e_type = evidence.get('type', 'unknown')
        
        if e_type == 'chat':
            quote = evidence.get('quote', '')
            context = evidence.get('context', '')
            source = evidence.get('file', '')
            st.markdown(f"> _{quote}_" if quote else f"> {context}")
            if source:
                source_label = L('source', 'Source')
                st.caption(f"{source_label}: {source}")
        
        elif e_type == 'call':
            date = evidence.get('date', '')
            desc = evidence.get('description', '')
            context = evidence.get('context', '')
            st.markdown(f"📞 **{date}** — {desc}")
            if context:
                st.caption(context)


def render_expandable_claim(violation_key, violation_data, evidence_dir, labels=None):
    """Render a clean, minimal legal claim with tabbed evidence."""
    _l = labels or {}
    def L(key, default):
        return _l.get(key, default)

    law_code = violation_data.get('law_code', '')
    title = violation_data.get('title', '')
    description = violation_data.get('description', '')
    evidence_list = violation_data.get('evidence', [])
    
    # Clean expander label with proper prefix
    if labels:
        # Check if it's German or Portuguese based on common label
        if L('legal_basis', 'Legal basis') == 'Rechtsgrundlage':
            prefix = "GESETZ"
        else:
            prefix = "LEI"
    else:
        prefix = "LAW"
    expander_label = f"{prefix}: {law_code} — {title}"
    claim_id = _stable_key_id(violation_key)

    with st.expander(expander_label, expanded=False):
        # Brief legal summary (no red error box - just clean text)
        legal_basis_label = L('legal_basis', 'Legal basis')
        st.markdown(f"**{legal_basis_label}:** {description}")
        st.write("")
        
        # Categorize evidence
        images = [e for e in evidence_list if e.get('type') == 'image']
        documents = [e for e in evidence_list if e.get('type') in ['pdf', 'document']]
        other = [e for e in evidence_list if e.get('type') in ['chat', 'call']]
        
        # Count for tabs
        has_images = len(images) > 0
        has_docs = len(documents) > 0
        has_other = len(other) > 0
        
        # Build tab list dynamically
        tab_names = []
        if has_images:
            tab_names.append(f"{L('screenshots', 'Screenshots')} ({len(images)})")
        if has_docs:
            tab_names.append(f"{L('documents', 'Documents')} ({len(documents)})")
        if has_other:
            tab_names.append(f"{L('communications', 'Communications')} ({len(other)})")
        
        if not tab_names:
            st.caption(L('no_evidence', 'No evidence attached.'))
            return
        
        tabs = st.tabs(tab_names)
        tab_idx = 0
        
        if has_images:
            with tabs[tab_idx]:
                gallery_images = [{
                    "path": Path(evidence_dir) / ev.get('file', ''),
                    "context": ev.get('context', ''),
                    "description": ev.get('description', ''),
                    "file": ev.get('file', ''),
                } for ev in images]
                _render_image_gallery(gallery_images, claim_id, L)
            tab_idx += 1
        
        if has_docs:
            with tabs[tab_idx]:
                _render_documents_compact(documents, claim_id, evidence_dir, L)
            tab_idx += 1
        
        if has_other:
            with tabs[tab_idx]:
                _render_other_evidence_compact(other, claim_id, L)
