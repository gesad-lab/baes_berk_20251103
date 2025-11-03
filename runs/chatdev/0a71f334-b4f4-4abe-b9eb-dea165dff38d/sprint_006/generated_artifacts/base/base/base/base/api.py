'''
API endpoints for managing students.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate, StudentResponse
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        db_student = Student(name=student.name, email=student.email)  # Update this line
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        students = db.query(Student).offset(skip).limit(limit).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))