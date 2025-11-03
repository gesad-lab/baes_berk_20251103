'''
Defines the API routes for course operations.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Course
from schemas import CourseCreate, CourseResponse
router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Include teacher_id
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course