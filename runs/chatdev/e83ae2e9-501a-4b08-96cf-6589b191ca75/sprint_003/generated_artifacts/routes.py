'''
Defines the API routes for the Course entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Course
from database import get_db
from pydantic import BaseModel
router = APIRouter()
class CourseCreate(BaseModel):
    name: str
    level: str
@router.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@router.get("/courses/", response_model=list[CourseCreate])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of courses from the database.
    '''
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses