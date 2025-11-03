'''
Defines the API routes for the Student entity.
'''
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student
from schemas import StudentCreate, StudentResponse
student_router = APIRouter()
@student_router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return db_student
@student_router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int):
    db: Session = SessionLocal()
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db.close()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student