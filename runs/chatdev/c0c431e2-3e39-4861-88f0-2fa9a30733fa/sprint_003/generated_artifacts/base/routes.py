'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from pydantic import BaseModel
# Pydantic model for request validation
class StudentCreate(BaseModel):
    name: str
    email: str  # New email field
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Creates a new student.
    '''
    new_student = Student(name=student.name, email=student.email)  # Include email
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id, "name": new_student.name, "email": new_student.email}
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieves all students.
    '''
    return db.query(Student).all()