'''
Router for handling course-related API endpoints.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import CourseCreate, CourseResponse
from crud import create_course, get_courses
from database import get_db
router = APIRouter()
@router.post("/courses/", response_model=CourseResponse)
def create_course_endpoint(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)
@router.get("/courses/", response_model=list[CourseResponse])
def read_courses(db: Session = Depends(get_db)):
    return get_courses(db=db)