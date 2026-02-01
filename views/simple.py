# Simple timeline - follow-up of all eras with images
import streamlit as st
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

BASE_DIR = Path(__file__).parent.parent


# Eras: high-level follow-up (on start = order recurring, they ask 150/shipping, etc.)
SIMPLE_ERAS = [
    {
        "date": "2025-11",
        "title": "Start — Order recurring",
        "desc": "Subscription begins. Orders #15073, #15179 confirmed. Weekly 70L milk, 20% discount, free shipping (€0).",
        "image": None,
    },
    {
        "date": "2025-11-19",
        "title": "They ask for extra payment (shipping)",
        "desc": "Order #15073 update: payment of €19.90 due — \"adjustments to shipping fee\" or refrigerated/express. Not agreed at checkout.",
        "image": None,
    },
    {
        "date": "2025-12",
        "title": "Recurring orders & consolidation",
        "desc": "Order #15341 (180L consolidated). Customer asked to skip next week. System delayed/cancelled weekly orders.",
        "image": None,
    },
    {
        "date": "2025-12",
        "title": "Subscription cancelled",
        "desc": "Subscription cancelled by merchant. Later orders #15977, #16045 with new terms and surcharges.",
        "image": None,
    },
    {
        "date": "2026-01-10",
        "title": "Order #15977 — shipping surcharge €39.90",
        "desc": "Order update: \"Surcharge Heavy Voluminous Shipping\" €39.90 added after confirmation.",
        "image": None,
    },
    {
        "date": "2026-01-16",
        "title": "Order #16045 — pricing & payment",
        "desc": "Order #16045 confirmed; pricing and payment evidence. Total €473.85 disputed.",
        "images": [
            "WhatsApp Image 2026-01-16 at 00.40.52.jpeg",
            "WhatsApp Image 2026-01-16 at 00.41.58.jpeg",
        ],
    },
    {
        "date": "2026-01-20",
        "title": "Terms & default notice",
        "desc": "Declaration of default (Verzug). Rejection of unilateral refund. ToS/shipping policy.",
        "image": "WhatsApp Image 2026-01-20 at 14.16.30 (1).jpeg",
    },
    {
        "date": "2026-01-21",
        "title": "Legal follow-up",
        "desc": "Empty email / WhatsApp follow-up. Binding confirmation, reinstated agreement.",
        "image": "WhatsApp Image 2026-01-21 at 19.16.03 (1).jpeg",
    },
]


def _resolve_image(rel_path):
    if not rel_path:
        return None
    p = BASE_DIR / rel_path.strip()
    if p.exists():
        ext = p.suffix.lower()
        if ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
            return str(p)
    return None


def render_simple_page():
    """Render the simple timeline: follow-up of all eras with images."""
    st.markdown("# Simple — Timeline")
    st.markdown("Follow-up of all eras: on start order recurring, they ask for shipping, the events.")
    st.write("")

    for i, era in enumerate(SIMPLE_ERAS):
        with st.container(border=True):
            col_img, col_txt = st.columns([1, 2])
            with col_txt:
                st.subheader(f"📅 {era['date']} — {era['title']}")
                st.caption(era["date"])
                st.write(era["desc"])
            with col_img:
                img_paths = era.get("images") or ([era.get("image")] if era.get("image") else [])
                shown = False
                for img_path in img_paths:
                    if not img_path:
                        continue
                    resolved = _resolve_image(img_path)
                    if resolved:
                        st.image(resolved, use_container_width=True, caption=Path(img_path).name)
                        shown = True
                if not shown:
                    st.caption("_No image_")
        st.write("")

    st.divider()
    st.caption("Simple timeline — key eras only. Use **Timeline** for full event list.")


if __name__ == "__main__":
    render_simple_page()
