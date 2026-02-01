# Violations View - Legal Argument Analysis (German/EU and Portugal versions)
import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from data.evidence_mapping import EVIDENCE_MAP
from data.violations_locale import (
    VIOLATION_KEYS_ORDER,
    get_overview,
    get_stats,
    get_violation_data_for_locale,
)
from components.expandable_claim import render_expandable_claim

EVIDENCE_DIR = Path(__file__).parent.parent

# Key legal communication extracts (data/eml_extract_*.md) – displayed on violations page
KEY_LEGAL_EXTRACTS = [
    ("data/eml_extract_default_notice_2026_01_20.md", "Declaration of Default (Verzug) – 20 Jan 2026"),
    ("data/eml_extract_refund_rejection_2026_01_20.md", "Rejection of Unilateral Refund – 20 Jan 2026"),
    ("data/eml_extract_binding_confirmation_2026_01_22.md", "Binding Confirmation – Reinstated Subscription – 22 Jan 2026"),
]


def _render_key_legal_communications(evidence_dir, is_pt=False, is_de=False):
    """Render Key Legal Communications as a clean dropdown."""
    if is_pt:
        section_title = "Comunicações Legais Principais"
    elif is_de:
        section_title = "Wichtige rechtliche Mitteilungen"
    else:
        section_title = "Key Legal Communications"
    with st.expander(section_title, expanded=False):
        for rel_path, title in KEY_LEGAL_EXTRACTS:
            full_path = evidence_dir / rel_path
            content = None
            if full_path.exists():
                try:
                    content = full_path.read_text(encoding="utf-8")
                except Exception:
                    pass
            
            with st.expander(f"📄 {title}", expanded=False):
                if content:
                    st.markdown(content)
                else:
                    if is_pt:
                        st.caption("Ficheiro não encontrado.")
                    elif is_de:
                        st.caption("Datei nicht gefunden.")
                    else:
                        st.caption("File not found.")
                
                if is_de:
                    button_text = "Herunterladen"
                else:
                    button_text = "Download"
                
                st.download_button(
                    button_text,
                    (content or "").encode("utf-8"),
                    Path(rel_path).name,
                    mime="text/markdown",
                    key=f"key_comms_dl_{Path(rel_path).stem}",
                    disabled=(not content),
                )


def render_violations_page(jurisdiction="de_eu"):
    """Render the legal violations analysis. jurisdiction: 'de_eu', 'de' (German), or 'pt'."""
    is_pt = jurisdiction == "pt"
    is_de = jurisdiction == "de"

    # Page title
    if is_pt:
        st.markdown("# Relatório de Violações à Proteção do Consumidor")
    elif is_de:
        st.markdown("# Bericht über Verstöße gegen Verbraucherschutzgesetze")
    else:
        st.markdown("# Consumer Protection Violation Report")
    
    stats = get_stats(jurisdiction)
    # Compact stats row
    c1, c2, c3 = st.columns(3)
    with c1:
        if is_pt:
            st.metric("Violações", len(VIOLATION_KEYS_ORDER))
        elif is_de:
            st.metric("Verstöße", len(VIOLATION_KEYS_ORDER))
        else:
            st.metric("Violations", len(VIOLATION_KEYS_ORDER))
    with c2:
        if is_pt:
            st.metric("Lei", stats["applicable_law"])
        elif is_de:
            st.metric("Rechtsgrundlage", stats["applicable_law"])
        else:
            st.metric("Law", stats["applicable_law"])
    with c3:
        if is_pt:
            st.metric("Jurisdição", stats["jurisdiction"])
        elif is_de:
            st.metric("Gerichtsbarkeit", stats["jurisdiction"])
        else:
            st.metric("Jurisdiction", stats["jurisdiction"])
    
    st.divider()
    
    # Executive Summary - collapsible
    if is_pt:
        summary_title = "Sumário Executivo"
    elif is_de:
        summary_title = "Zusammenfassung"
    else:
        summary_title = "Executive Summary"
    
    with st.expander(summary_title, expanded=False):
        st.markdown(get_overview(jurisdiction))
    
    st.write("")
    labels = None
    if jurisdiction in ["pt", "de"]:
        from data.violations_locale import get_labels
        labels = get_labels(jurisdiction)

    # Render Violations
    for violation_key in VIOLATION_KEYS_ORDER:
        violation_data = get_violation_data_for_locale(violation_key, jurisdiction)
        render_expandable_claim(violation_key, violation_data, EVIDENCE_DIR, labels=labels)

    # Key Legal Communications
    st.divider()
    _render_key_legal_communications(EVIDENCE_DIR, is_pt, is_de)

if __name__ == "__main__":
    render_violations_page()
