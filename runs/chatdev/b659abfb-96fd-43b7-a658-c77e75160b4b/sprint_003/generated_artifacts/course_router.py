'''
Defines the API routes for course management.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Course
from schemas import CourseCreate, CourseResponse
router = APIRouter()
@router.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    # Use a context manager to handle the session
    with SessionLocal() as db:
        db_course = Course(name=course.name, level=course.level)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return db_course