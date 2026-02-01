"""
Consumer Protection Violation Report
Comprehensive documentation of regulatory violations for submission to competent authorities.
"""

import streamlit as st
from pathlib import Path
import sys

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

from components.styles import get_styles
from views.violations import render_violations_page
from data.violations_locale import JURISDICTION_OPTIONS, DEFAULT_JURISDICTION

# Page configuration
st.set_page_config(
    page_title="Consumer Protection Violation Report",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS styling
st.markdown(get_styles(), unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("# Regulatory Complaint Submission")
    # Use native markdown to avoid custom HTML divs (prevents React removeChild DOM sync errors)
    st.caption("📦 Documentation Package")
    
    st.write("")
    
    st.markdown("### Document Type")
    # Violations only; dashboard hidden
    page = st.radio(
        "Select View",
        ["Violation Report"],
        label_visibility="collapsed",
        key="sidebar_page",
    )

    # Law / Jurisdiction switch (easy to change in code: edit data.violations_locale)
    jurisdiction = None
    if "Violation" in page:
        st.markdown("### Applicable Legal Framework")
        jurisdiction = st.radio(
            "Jurisdiction",
            ["de_eu", "de", "pt"],
            format_func=lambda x: (
                "German/EU Law (BGB/UWG) - English" if x == "de_eu" 
                else "German/EU Law (BGB/UWG) - Deutsch" if x == "de"
                else "Portuguese/EU Law (DL 24/2008, DL 57/2008)"
            ),
            index=JURISDICTION_OPTIONS.index(DEFAULT_JURISDICTION),
            label_visibility="collapsed",
            key="sidebar_jurisdiction",
        )

# Routing: render in fragment so expand/collapse only reruns this block (reduces removeChild DOM errors)
_j = jurisdiction or DEFAULT_JURISDICTION
if hasattr(st, "fragment"):

    @st.fragment
    def _violations_fragment():
        render_violations_page(_j)

    _violations_fragment()
else:
    render_violations_page(_j)

# Global Footer (native elements only to avoid React removeChild errors)
st.divider()
st.caption("Regulatory Complaint Documentation | All evidence authenticated and preserved for submission to competent authorities")
