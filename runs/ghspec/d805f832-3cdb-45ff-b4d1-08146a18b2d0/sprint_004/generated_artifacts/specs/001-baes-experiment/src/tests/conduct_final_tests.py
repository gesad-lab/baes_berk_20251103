```python
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Course, Base  # Importing the Course model from models
import pytest

# Initialize the FastAPI application
app = FastAPI()

# SQLite database connection settings
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test endpoint documentation
@app.post("/students/{student_id}/courses", response_model=dict)
async def associate_course(student_id: int, course: dict):
    """
    Associate an existing Course with a Student.

    Request:
        - URL: /students/{student_id}/courses
        - Method: POST
        - Body: JSON object containing a course_id
        Example:
        {
            "course_id": 1
        }

    Response:
        - Success: JSON object confirming the association and returning the updated list of courses.
        Example:
        {
            "message": "Course successfully associated.",
            "updated_courses": [
                {"id": 1, "name": "Mathematics"},
                {"id": 2, "name": "Science"}
            ]
        }
        - Error (404): JSON object indicating that the Course cannot be found.
        Example:
        {
            "detail": "Course not found."
        }
    """
    # Simulating course association logic and response
    return {"message": "Course successfully associated.", "updated_courses": []}  # Placeholder implementation

@app.get("/students/{student_id}/courses", response_model=dict)
async def retrieve_courses(student_id: int):
    """
    Retrieve all courses associated with a Student.

    Request:
        - URL: /students/{student_id}/courses
        - Method: GET

    Response:
        - JSON object containing an array of courses associated with the specified Student.
        Example:
        {
            "courses": [
                {"id": 1, "name": "Mathematics"},
                {"id": 2, "name": "Science"}
            ]
        }
    """
    # Simulating course retrieval logic
    return {"courses": []}  # Placeholder implementation

# Unit tests for the new endpoints will follow
```