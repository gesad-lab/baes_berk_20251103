```python
# src/services/course_service.py

from pydantic import BaseModel, Field, constr
from typing import List
from src.repository import Course, get_db_session
from sqlalchemy.orm import Session
from fastapi import HTTPException

class CourseCreate(BaseModel):
    name: constr(min_length=1, max_length=100) = Field(..., description="The name of the course, which cannot be empty.")
    level: constr(min_length=1, max_length=50) = Field(..., description="The level of the course, which cannot be empty.")

class CourseService:
    def __init__(self, db: Session):
        self.db = db

    def create_course(self, course: CourseCreate) -> Course:
        # Create and save a new Course entity
        new_course = Course(name=course.name, level=course.level)
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        return new_course

    def get_courses(self) -> List[Course]:
        # Retrieve all Course records from the database
        courses = self.db.query(Course).all()
        return courses

def get_course_service() -> CourseService:
    db = get_db_session()  # Assuming get_db_session returns a valid database session
    return CourseService(db)
```