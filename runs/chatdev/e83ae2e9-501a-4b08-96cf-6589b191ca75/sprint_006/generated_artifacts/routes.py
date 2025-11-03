'''
Defines the API routes for the Teacher and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Teacher, Course  # Ensure Course model is imported
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
router = APIRouter()
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation
@router.post("/teachers/", response_model=TeacherCreate)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Create a new teacher in the database.
    '''
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@router.get("/teachers/", response_model=list[TeacherCreate])
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of teachers from the database.
    '''
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Add teacher_id to the course creation model
@router.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database with an associated teacher.
    '''
    # Check if the teacher exists
    if not db.query(Teacher).filter(Teacher.id == course.teacher_id).first():
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)
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