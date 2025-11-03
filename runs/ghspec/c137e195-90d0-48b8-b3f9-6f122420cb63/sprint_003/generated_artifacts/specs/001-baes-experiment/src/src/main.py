from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from database.db import init_db
from api.students import router as student_router

app = FastAPI()

class ErrorResponse(BaseModel):
    error: dict

@app.on_event("startup")
def startup():
    """Initialize the database on application startup."""
    init_db()

app.include_router(student_router)

# Error handling functions
def handle_missing_email():
    """Raises an HTTP exception for missing email."""
    raise HTTPException(status_code=400, detail="Email is required")

# Centralized error handling for course-related errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handles HTTP exceptions and returns structured error responses."""
    return ErrorResponse(error={
        "code": f"E{exc.status_code:03}",
        "message": exc.detail
    }).dict()  # Returning as a dictionary to convert to JSON automatically

# Include the new error handling for creating courses in a new router
from api.courses import router as course_router

app.include_router(course_router)