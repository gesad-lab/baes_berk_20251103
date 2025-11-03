'''
Defines the API routes for student operations.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student
from schemas import StudentCreate, StudentResponse
router = APIRouter()
@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    db_student = Student(name=student.name, email=student.email)  # Added email to student creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return db_student