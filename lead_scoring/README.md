# Lead Scoring Backend

## Setup
1. Create virtual environment:
   python -m venv venv
   activate it:
   - Windows: venv\Scripts\activate
   - Linux/Mac: source venv/bin/activate
2. Install dependencies:
   pip install -r requirements.txt

## Run server
uvicorn app.main:app --reload --port 8000

## Test APIs
- http://127.0.0.1:8000/docs  (Swagger UI)
