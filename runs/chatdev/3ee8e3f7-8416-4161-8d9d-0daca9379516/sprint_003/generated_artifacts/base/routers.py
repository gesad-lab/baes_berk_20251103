'''
API routes for student-related operations.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from schemas import StudentCreate, StudentResponse
router = APIRouter()
@router.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student in the database.
    """
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    """
    Retrieve all students from the database.
    """
    students = db.query(Student).all()
    return students