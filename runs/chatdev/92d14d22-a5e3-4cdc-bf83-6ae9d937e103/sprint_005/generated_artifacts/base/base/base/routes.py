'''
API routes for handling student-related requests.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from schemas import StudentCreate, StudentResponse
student_router = APIRouter()
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Update this line
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@student_router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students