"""
main.py

This module serves as the entry point for the FastAPI application, defining the routes and handling HTTP requests related to courses and teachers. 
It includes endpoints to assign a teacher to a course and retrieve course information along with teacher assignments.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.models.course import Course
from src.models.teacher import Teacher
from src.database.database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CourseUpdate(BaseModel):
    teacher_id: Optional[int] = None

@app.put("/courses/{course_id}", response_model=Course)
def assign_teacher_to_course(course_id: int, course_update: CourseUpdate, db: Session = next(get_db())):
    """
    Assign a teacher to a specific course.

    - **course_id**: An integer representing the unique identifier of the Course.
    - **course_update**: A CourseUpdate model that includes the teacher_id to be assigned.

    Returns the updated Course details including the associated Teacher information.
    Raises HTTP 400 if required fields are missing.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    if course_update.teacher_id is not None:
        course.teacher_id = course_update.teacher_id

    db.commit()
    db.refresh(course)
    
    return course

@app.get("/courses/{course_id}", response_model=Course)
def get_course_details(course_id: int, db: Session = next(get_db())):
    """
    Retrieve course information, including the assigned teacher.

    - **course_id**: An integer representing the unique identifier of the Course.

    Returns the Course details in JSON format, including the associated Teacher information.
    Raises HTTP 404 if the Course is not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course

# Additional code for existing endpoints can be added here...
"""