'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: EmailStr  # Add email field with validation
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: Student, db: Session = Depends(get_db)):
    '''
    Creates a new student with the given name and email.
    '''
    new_student = StudentModel(name=student.name, email=student.email)  # Include email
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id, "name": new_student.name, "email": new_student.email}  # Return email
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieves all students.
    '''
    return db.query(StudentModel).all()