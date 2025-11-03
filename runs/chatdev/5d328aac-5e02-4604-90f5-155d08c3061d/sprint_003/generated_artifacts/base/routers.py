'''
Defines the API routes for the Student entity.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_student, get_students
from schemas import StudentCreate, StudentResponse
router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/students/", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)
@router.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)