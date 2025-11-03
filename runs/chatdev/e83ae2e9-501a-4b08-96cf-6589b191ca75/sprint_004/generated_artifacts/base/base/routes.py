'''
Defines the API routes for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from pydantic import BaseModel
router = APIRouter()
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
@router.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Check for duplicate student names
    existing_student = db.query(Student).filter(Student.name == student.name).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this name already exists.")
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@router.get("/students/", response_model=list[StudentCreate])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students