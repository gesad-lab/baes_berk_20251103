'''
Contains the API endpoints for managing Student entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
router = APIRouter()
@router.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email in creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentCreate(name=db_student.name, email=db_student.email)  # Return email
@router.get("/students/", response_model=list[StudentCreate])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return [StudentCreate(name=student.name, email=student.email) for student in students]  # Return email