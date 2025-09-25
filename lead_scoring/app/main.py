# app/main.py

from fastapi import FastAPI
from app import routes  # import our API routes

# Create FastAPI app
app = FastAPI(
    title="Lead Scoring API",
    description="Backend service for scoring leads using rules + AI",
    version="1.0.0"
)

# Include routes from routes.py
app.include_router(routes.router)

# Root endpoint (health check)
@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running!"}
