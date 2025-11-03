'''
Contains the FastAPI routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(name: str, email: str, db: Session = Depends(get_db)):  # Updated to accept email
    db_student = Student(name=name, email=email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Updated response
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Updated to include email