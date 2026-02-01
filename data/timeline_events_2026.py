# Timeline Events 2026 - Comprehensive from all PDFs and communications
# Split into two files to keep under 500 lines each
from data.timeline_events_2026_jan_early import TIMELINE_EVENTS_2026_JAN_EARLY
from data.timeline_events_2026_jan_late import TIMELINE_EVENTS_2026_JAN_LATE
from data.timeline_events_2026_jan_email_notifications import TIMELINE_EVENTS_2026_EMAILS
from data.timeline_events_2026_feb import TIMELINE_EVENTS_2026_FEB

TIMELINE_EVENTS_2026 = (
    TIMELINE_EVENTS_2026_JAN_EARLY
    + TIMELINE_EVENTS_2026_JAN_LATE
    + TIMELINE_EVENTS_2026_EMAILS
    + TIMELINE_EVENTS_2026_FEB
)
