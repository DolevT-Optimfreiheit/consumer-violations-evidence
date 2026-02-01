# Timeline page - Professional Audit Log
import streamlit as st
from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent.parent))

from utils.file_utils import get_pdf_summary
from data.evidence_loader import get_all_evidence
from data.timeline_events import get_timeline_events

def render_timeline_page():
    """Render the timeline view"""
    
    st.markdown("# 📅 Case Timeline")
    st.markdown("View all events in chronological order")
    st.write("")
    
    # Load all evidence for context
    all_evidence = get_all_evidence()
    evidence_lookup = {}
    for cat, files in all_evidence.items():
        for f in files:
            evidence_lookup[f['name']] = f
    
    # Timeline events - Comprehensive from all PDFs and communications
    timeline_events = get_timeline_events()
    
    type_icons = {
        'order': '📦',
        'communication': '💬',
        'incident': '⚡',
        'legal': '⚖️',
        'critical': '🚨',
        'evidence': '📎',
    }
    
    # Simplified Filters in an expander
    with st.expander("🔍 Filter & Search", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            all_types = sorted({e.get("type", "document") for e in timeline_events})
            type_filter = st.multiselect("Event Type", all_types, default=all_types)
        
        with col2:
            text_filter = st.text_input("Search", placeholder="Search events...")
        
        with col3:
            dates = sorted({e["date"] for e in timeline_events if e.get("date")})
            date_start = dates[0] if dates else None
            date_end = dates[-1] if dates else None
            date_range = st.text_input("Date Range", value=f"{date_start} to {date_end}", 
                                      help="Format: YYYY-MM-DD to YYYY-MM-DD")
        
        col4, col5, col6 = st.columns(3)
        
        with col4:
            oldest_first = st.checkbox("Show oldest first", value=False)
        
        with col5:
            only_with_evidence = st.checkbox("Only events with evidence", value=False)
        
        with col6:
            only_with_violation = st.checkbox("Only violations", value=False)
        
        col7, col8 = st.columns(2)
        
        with col7:
            group_by_date = st.checkbox("Group by date", value=True)
        
        with col8:
            show_evidence_previews = st.checkbox("Show evidence previews", value=False)
    
    expand_all_groups = False  # Simplified: don't show this option

    def in_date_range(date_str, range_str):
        if not range_str or "to" not in range_str:
            return True
        try:
            start_str, end_str = [s.strip() for s in range_str.split("to", 1)]
            return start_str <= date_str <= end_str
        except Exception:
            return True

    # Sort & filter events
    sorted_events = sorted(timeline_events, key=lambda x: x.get('date', ''), reverse=not oldest_first)
    filtered_events = []
    for event in sorted_events:
        if event.get("type") not in type_filter:
            continue
        if not in_date_range(event.get("date", ""), date_range):
            continue
        if only_with_evidence and not event.get("evidence"):
            continue
        if only_with_violation and not event.get("violation"):
            continue
        if text_filter:
            ev_files = " ".join(event.get("evidence", []) or [])
            hay = f"{event.get('title','')} {event.get('desc','')} {event.get('summary','')} {event.get('details','')} {ev_files}".lower()
            if text_filter.lower() not in hay:
                continue
        filtered_events.append(event)

    # Quick stats
    st.write("")
    stats_cols = st.columns(4)
    stats_cols[0].metric("Total Events", len(filtered_events))
    stats_cols[1].metric("Legal Events", sum(1 for e in filtered_events if e.get("type") == "legal"))
    stats_cols[2].metric("Critical Events", sum(1 for e in filtered_events if e.get("type") == "critical"))
    stats_cols[3].metric("Incidents", sum(1 for e in filtered_events if e.get("type") == "incident"))
    st.write("")

    if filtered_events:
        csv_lines = ["date,title,type,violation,desc,evidence"]
        for e in filtered_events:
            evidence = "|".join(e.get("evidence", []) or [])
            row = [
                e.get("date", ""),
                e.get("title", "").replace('"', '""'),
                e.get("type", ""),
                e.get("violation", ""),
                (e.get("desc", "") or e.get("summary", "") or "").replace('"', '""'),
                evidence.replace('"', '""'),
            ]
            csv_lines.append(f"\"{row[0]}\",\"{row[1]}\",\"{row[2]}\",\"{row[3]}\",\"{row[4]}\",\"{row[5]}\"")
        st.download_button(
            "📥 Export Timeline to CSV",
            "\n".join(csv_lines).encode("utf-8"),
            "timeline_export.csv",
            mime="text/csv",
        )
    
    def render_event_card(event, event_idx):
        icon = type_icons.get(event['type'], '📄')
        
        with st.container(border=True):
            # Title and Date
            st.markdown(f"### {icon} {event['title']}")
            st.caption(f"📅 {event['date']} • 🏷️ {event.get('type', 'document').title()}")
            
            if event.get("violation"):
                st.warning(f"⚠️ **Legal Violation:** {event['violation']}")
            
            # Handle both 'desc' and 'summary'/'details' formats with compact display
            desc = event.get('desc')
            summary = event.get('summary')
            details = event.get('details')
            if not summary and desc:
                if len(desc) > 200:
                    summary = desc[:200].rsplit(' ', 1)[0] + "..."
                    if not details:
                        details = desc
                else:
                    summary = desc
            if summary:
                st.markdown(summary)
            
            # Expanders for details
            if details or event.get('details') or event.get('evidence'):
                with st.expander("📋 View Full Details"):
                    if details:
                        st.markdown(details)
                    elif event.get('details'):
                        st.markdown(event['details'])
                    
                    if event.get('evidence'):
                        st.write("")
                        st.markdown("**📎 Supporting Evidence:**")
                        base_dir = Path(__file__).parent.parent
                        for ev_idx, ev in enumerate(event['evidence']):
                            file_path = base_dir / ev
                            file_info = evidence_lookup.get(ev, {})
                            file_description = file_info.get('description', '')
                            
                            if not show_evidence_previews:
                                st.caption(f"• {ev}")
                                if file_description:
                                    st.caption(f"  _{file_description}_")
                                continue

                            if file_path.exists():
                                    file_ext = file_path.suffix.lower()
                                    if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
                                        if file_description:
                                            st.caption(f"📋 {file_description}")
                                        st.image(str(file_path), caption=ev, use_container_width=True)
                                    elif file_ext == '.pdf':
                                        if file_description:
                                            st.info(f"📋 {file_description}")
                                        pdf_summary = get_pdf_summary(file_path)
                                        if pdf_summary:
                                            with st.expander(f"📄 Preview: {ev}"):
                                                st.text(pdf_summary)
                                        with open(file_path, "rb") as pdf_file:
                                            st.download_button(
                                                label=f"📄 Download {ev}",
                                                data=pdf_file.read(),
                                                file_name=ev,
                                                mime="application/pdf",
                                                key=f"timeline_pdf_{event_idx}_{ev_idx}"
                                            )
                                    elif file_ext in ['.txt', '.text']:
                                        with open(file_path, "rb") as txt_file:
                                            st.download_button(
                                                label=f"📝 {ev}",
                                                data=txt_file.read(),
                                                file_name=ev,
                                                mime="text/plain",
                                                key=f"timeline_txt_{event_idx}_{ev_idx}"
                                            )
                                    elif file_ext == '.md':
                                        try:
                                            md_content = file_path.read_text(encoding="utf-8")
                                            with st.expander(f"📄 {ev}"):
                                                st.markdown(md_content)
                                        except Exception:
                                            pass
                                        with open(file_path, "rb") as md_file:
                                            st.download_button(
                                                label=f"📥 Download {ev}",
                                                data=md_file.read(),
                                                file_name=ev,
                                                mime="text/markdown",
                                                key=f"timeline_md_{event_idx}_{ev_idx}"
                                            )
                                    elif file_ext == '' or ev == '2026-01-20-Default_Notice_Email_Content.txt' or 'default_notice' in ev.lower():
                                        try:
                                            with open(file_path, 'r', encoding='utf-8') as f:
                                                content = f.read()
                                                st.text_area(
                                                    f"📄 {ev}",
                                                    content,
                                                    height=200,
                                                    key=f"timeline_text_{event_idx}_{ev_idx}"
                                                )
                                        except:
                                            with open(file_path, "rb") as f:
                                                st.download_button(
                                                    label=f"📎 {ev}",
                                                    data=f.read(),
                                                    file_name=ev,
                                                    key=f"timeline_file_{event_idx}_{ev_idx}"
                                                )
                                    else:
                                        with open(file_path, "rb") as f:
                                            st.download_button(
                                                label=f"📎 {ev}",
                                                data=f.read(),
                                                file_name=ev,
                                                key=f"timeline_gen_{event_idx}_{ev_idx}"
                                            )
                            else:
                                st.caption(f"📎 {ev} (file not found)")

    st.write("")
    event_counter = 0
    if group_by_date:
        grouped = {}
        for event in filtered_events:
            grouped.setdefault(event.get("date", "Unknown"), []).append(event)
        grouped_dates = sorted(grouped.keys(), reverse=True)
        for idx, date_key in enumerate(grouped_dates):
            group_label = f"{date_key} • {len(grouped[date_key])} events"
            with st.expander(group_label, expanded=(expand_all_groups or idx == 0)):
                for event in grouped[date_key]:
                    render_event_card(event, event_counter)
                    event_counter += 1
    else:
        for event in filtered_events:
            render_event_card(event, event_counter)
            event_counter += 1

if __name__ == "__main__":
    render_timeline_page()
