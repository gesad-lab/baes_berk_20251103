```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import List
from models import Course  # Assuming Course model exists in models.py
from repository import CourseRepository  # Assuming CourseRepository exists
from database import get_db  # Assuming get_db function exists for database sessions

app = FastAPI()

# Pydantic model for request body validation
class CourseCreate(BaseModel):
    name: str = Field(..., example="Mathematics")
    level: str = Field(..., example="Beginner")

@app.post("/courses/", response_model=Course)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new Course in the database.
    
    :param course: CourseCreate model instance containing the course data.
    :param db: Database session.
    :raises HTTPException: If the course name already exists or other validation issues.
    :return: The created Course model instance.
    """
    # Check if the course name already exists to avoid duplication
    if CourseRepository.exists(db, name=course.name):
        raise HTTPException(status_code=400, detail="Course with this name already exists.")
    
    # Create new Course record
    new_course = Course(name=course.name, level=course.level)
    CourseRepository.create(db, new_course)
    
    return new_course

@app.get("/courses/", response_model=List[Course])
def get_courses(db: Session = next(get_db())):
    """
    Retrieve a list of all courses from the database.
    
    :param db: Database session.
    :return: List of Course model instances.
    """
    return CourseRepository.get_all(db)
```
