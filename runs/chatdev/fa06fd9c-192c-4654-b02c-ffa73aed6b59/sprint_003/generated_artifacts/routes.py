'''
Defines the API routes for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course  # Import Course model
from database import get_db
from pydantic import BaseModel, constr
class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Ensure name is not empty
    email: constr(min_length=1)  # Ensure email is not empty
class CourseCreate(BaseModel):
    name: constr(min_length=1)  # Ensure name is not empty
    level: constr(min_length=1)  # Ensure level is not empty
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list)
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()