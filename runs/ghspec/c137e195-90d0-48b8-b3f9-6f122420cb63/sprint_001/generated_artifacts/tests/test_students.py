from fastapi import FastAPI
from database.db import init_db
from api.students import router as student_router

app = FastAPI()

@app.on_event("startup")
def startup():
    """Initialize the database on application startup."""
    init_db()

app.include_router(student_router)