'''
Defines the API endpoints for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Add email field with validation
class CourseCreate(BaseModel):
    name: str
    level: str
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Return email
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Include email