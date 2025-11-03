'''
Defines the API routes for student management.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student
from schemas import StudentCreate, StudentResponse
router = APIRouter()
@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    # Use a context manager to handle the session
    with SessionLocal() as db:
        db_student = Student(name=student.name)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student