# consumer-violations-evidence

Documentation package for consumer protection violation complaints. Structured evidence, legal citations (German/EU and Portuguese/EU), and timeline events for submission to competent authorities.

## Run the app locally

Requires Python 3.10+.

```bash
pip install streamlit
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501).

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub.
3. New app → select this repo, main branch, `app.py` as main file.
4. Deploy. Your app will be live at `https://<your-app>.streamlit.app`.

## Project structure

- **`app.py`** — Streamlit entry point (Violation Report view).
- **`components/`** — UI (styles, expandable claims, image viewer).
- **`views/`** — Page rendering (violations).
- **`data/`** — Violations, evidence mapping, timeline events, locale (DE/EU, PT/EU).
- **`utils/`** — Helpers.

Evidence files (emails, images, PDFs) are referenced from `data/` and loaded at runtime.

## Legal frameworks

- **German/EU (BGB, UWG)** — English or Deutsch.
- **Portuguese/EU** — DL 24/2008, DL 57/2008, Código Civil, etc.

See `FINAL_STATUS_REPORT.md` and `FINAL_VERIFICATION_REPORT.md` for verification details.

---

## GitHub Pages

This repo includes a static **`index.html`** so you can enable GitHub Pages:

1. On GitHub: **Settings → Pages**.
2. Under **Source**, choose **Deploy from a branch**.
3. Branch: **main**, folder: **/ (root)**.
4. Save. The site will be at `https://dolevt-optimfreiheit.github.io/consumer-violations-evidence/`.

The Streamlit app does not run on GitHub Pages (static hosting only). The page explains how to run the app locally or deploy it on Streamlit Community Cloud.
