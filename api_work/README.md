# Clinical Task API

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.app:app --reload
```

## Routes
- `GET /v1/capabilities`
- `POST /v1/heartbeat`
- `POST /v1/task`

## Features
- CORS Support
- Logger Integration
- Exception Handling (Validation, HTTP, Unhandled)
- Modular Structure
- Pydantic Schemas
