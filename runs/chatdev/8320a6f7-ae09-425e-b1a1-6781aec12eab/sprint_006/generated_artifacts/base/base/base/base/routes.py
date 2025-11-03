'''
Defines the API endpoints for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel
from database import get_db
from pydantic import BaseModel
# Pydantic model for request validation
class Student(BaseModel):
    name: str
    email: str  # Added email field
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Added email field
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name, email=student.email)  # Added email to the model
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Added email to response
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(StudentModel).all()