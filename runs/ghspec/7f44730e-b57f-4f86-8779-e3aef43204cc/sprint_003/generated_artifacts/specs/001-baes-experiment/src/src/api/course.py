# src/api/course.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.course import Course

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses")
def create_course(course: CourseCreate):
    """
    Create a new course with the provided name and level.

    Parameters:
    - course: CourseCreate - The course object containing name and level.

    Returns:
    - A JSON response confirming the course creation or error details.
    """
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Both name and level are required"}})

    db = SessionLocal()
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return {"message": "Course created successfully", "course": {"name": db_course.name, "level": db_course.level}}

@router.get("/courses")
def get_courses():
    """
    Retrieve all the registered courses from the database.

    Returns:
    - A JSON list of courses including their names and levels.
    """
    db = SessionLocal()
    courses = db.query(Course).all()
    return {"courses": [{"name": course.name, "level": course.level} for course in courses]}

# API Documentation for Course Management
"""
## Course Management API

### Create a Course
- **Endpoint**: `POST /courses`
- **Description**: An administrator can create a new course.
- **Request Body**:
```json
{
    "name": "Introduction to Python",
    "level": "Beginner"
}
```
- **Response**:
```json
{
    "message": "Course created successfully",
    "course": {
        "name": "Introduction to Python",
        "level": "Beginner"
    }
}
```

### Retrieve Courses
- **Endpoint**: `GET /courses`
- **Description**: An administrator can retrieve all registered courses.
- **Response**:
```json
{
    "courses": [
        {
            "name": "Introduction to Python",
            "level": "Beginner"
        },
        {
            "name": "Advanced Database Systems",
            "level": "Intermediate"
        }
    ]
}
```
"""