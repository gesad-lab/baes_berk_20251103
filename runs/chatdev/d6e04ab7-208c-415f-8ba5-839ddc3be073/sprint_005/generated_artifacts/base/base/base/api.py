'''
Contains the API routes for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: EmailStr  # New email field added with validation
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: Student, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new student.
    '''
    db_student = StudentModel(name=student.name, email=student.email)  # Include email in creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Return email
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all students.
    '''
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Return email