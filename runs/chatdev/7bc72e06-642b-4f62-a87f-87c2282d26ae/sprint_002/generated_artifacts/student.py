'''
Router for handling student-related API endpoints.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import StudentCreate, StudentResponse
from crud import create_student, get_students
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)
@router.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)