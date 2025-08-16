# Cassper GPT

This Streamlit application provides a menu-driven interface for legal automation and case management. The menu items include:

- Chat GPT — chat with OpenAI's GPT API.
- Evidence Vault — upload and manage evidence securely.
- Timeline — visualize case timelines and events.
- Violation Scanner — scan documents for potential legal violations.
- Document Builder — generate legal documents and templates.
- FOIP Tools — tools for Freedom of Information and Protection requests.
- Alberta Forms — access Alberta-specific legal forms.
- Settings — configure application settings.

## Running locally

1. Clone this repo.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and set your `OPENAI_API_KEY`.
4. Run the app with:

```
streamlit run streamlit_app.py
```
