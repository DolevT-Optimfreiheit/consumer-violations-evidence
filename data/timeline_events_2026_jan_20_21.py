# Timeline Events 2026 - January 20-21 (Default Notice & Escalation Phase)
# Split into two files to keep under 500 lines each
from data.timeline_events_2026_jan_20_default import TIMELINE_EVENTS_2026_JAN_20_DEFAULT
from data.timeline_events_2026_jan_20_policy import TIMELINE_EVENTS_2026_JAN_20_POLICY
from data.timeline_events_2026_jan_20_policy_site import TIMELINE_EVENTS_2026_JAN_20_POLICY_SITE
from data.timeline_events_2026_jan_20_policy_dispute import TIMELINE_EVENTS_2026_JAN_20_POLICY_DISPUTE
from data.timeline_events_2026_jan_20_policy_environment import TIMELINE_EVENTS_2026_JAN_20_POLICY_ENVIRONMENT
from data.timeline_events_2026_jan_20_rejection import TIMELINE_EVENTS_2026_JAN_20_REJECTION

TIMELINE_EVENTS_2026_JAN_20_21 = (
    TIMELINE_EVENTS_2026_JAN_20_DEFAULT
    + TIMELINE_EVENTS_2026_JAN_20_POLICY
    + TIMELINE_EVENTS_2026_JAN_20_POLICY_SITE
    + TIMELINE_EVENTS_2026_JAN_20_POLICY_DISPUTE
    + TIMELINE_EVENTS_2026_JAN_20_POLICY_ENVIRONMENT
    + TIMELINE_EVENTS_2026_JAN_20_REJECTION
)
