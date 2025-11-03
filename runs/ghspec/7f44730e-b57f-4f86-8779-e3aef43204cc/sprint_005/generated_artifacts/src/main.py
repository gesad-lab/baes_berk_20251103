# src/main.py
from fastapi import FastAPI
from db.database import init_db
# Import new teachers API routes
import api.teachers  # New teachers module

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

# Register teachers routes
app.include_router(api.teachers.router)  # Include teacher routes for handling teacher-related requests