from pathlib import Path
from email import policy
from email.parser import BytesParser
import re


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", text)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ").replace("&#160;", " ")
    text = text.replace("&amp;", "&")
    return text


def extract_text(msg) -> str:
    parts = []
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ("text/plain", "text/html"):
                payload = part.get_payload(decode=True) or b""
                text = payload.decode(
                    part.get_content_charset() or "utf-8", errors="ignore"
                )
                if part.get_content_type() == "text/html":
                    text = strip_html(text)
                parts.append(text)
    else:
        payload = msg.get_payload(decode=True) or b""
        text = payload.decode(msg.get_content_charset() or "utf-8", errors="ignore")
        if msg.get_content_type() == "text/html":
            text = strip_html(text)
        parts.append(text)
    return "\n".join(parts)


path = Path(
    "Re  New customer message on November 17, 2025 at 5 14 pm - Dolev Tenenboim (dolev.tenenboim@gmail.com) - 2025-12-12 1926.eml"
)
print(path.exists())
if path.exists():
    msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
    body = extract_text(msg)
    lines = [re.sub(r"\s+", " ", l).strip() for l in body.replace("\r", "\n").split("\n") if l.strip()]
    for line in lines[:40]:
        safe = line.encode("ascii", errors="backslashreplace").decode("ascii")
        print(safe)
