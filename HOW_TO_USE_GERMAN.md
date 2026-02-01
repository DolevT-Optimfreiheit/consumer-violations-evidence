# How to Use German Language Version

## Quick Start

### Method 1: Use Sidebar (Recommended)

1. Run the application: `streamlit run app.py`
2. Look at the **left sidebar**
3. Under "**Applicable Legal Framework**", select:
   - `German/EU Law (BGB/UWG) - Deutsch` ✅

**Options:**
- `German/EU Law (BGB/UWG) - English` = English interface
- `German/EU Law (BGB/UWG) - Deutsch` = German interface (NEW!)
- `Portuguese/EU Law (DL 24/2008...)` = Portuguese interface

---

### Method 2: Set Default to German

**File:** `data/violations_locale.py`

**Change line 8:**
```python
# Before:
DEFAULT_JURISDICTION = "de_eu"

# After:
DEFAULT_JURISDICTION = "de"
```

Then run the app - it will default to German!

---

## What You'll See in German

### Page Elements:
- **Title:** Bericht über Verstöße gegen Verbraucherschutzgesetze
- **Metrics:** Verstöße, Rechtsgrundlage, Gerichtsbarkeit
- **Summary:** Zusammenfassung
- **Communications:** Wichtige rechtliche Mitteilungen

### Law Labels:
```
GESETZ: § 242 BGB — Verstoß gegen Treu und Glauben
  Rechtsgrundlage: Der Händler kontaktierte...
  
  [Bildschirmfotos (6) | Dokumente (3) | Kommunikationen (1)]
       ◀ Zurück  2 von 6  Weiter ▶
```

### All 7 Violations in German:
1. **§ 242 BGB** — Verstoß gegen Treu und Glauben
2. **§ 312j BGB** — Verstoß gegen die Button-Lösung  
3. **§ 305c BGB** — Überraschende Klausel
4. **§ 312a Abs. 3 BGB** — Unzulässige Nachzahlungspflichten
5. **§ 5 UWG** — Irreführende Werbung und Drip Pricing
6. **EU-Richtlinie 2005/29/EG** — Aggressive Geschäftspraktik
7. **§ 433 BGB** — Wesentliche Vertragsverletzung

---

## Verification

If you still see English:
1. Check the sidebar selection (make sure it says "Deutsch")
2. Refresh the page
3. Clear browser cache if needed

---

## Screenshots

**Before (English):**
```
LAW: § 242 BGB — Bad Faith Inducement
Legal basis: The merchant contacted...
[Screenshots (6) | Documents (3)]
```

**After (German):**
```
GESETZ: § 242 BGB — Verstoß gegen Treu und Glauben  
Rechtsgrundlage: Der Händler kontaktierte...
[Bildschirmfotos (6) | Dokumente (3)]
```

---

**Ready for submission to Verbraucherzentrale!** 🇩🇪
