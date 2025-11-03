'''
Defines the API routes for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from schemas import StudentCreate  # Import the Pydantic model
router = APIRouter()
@router.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if not student.name:
        raise HTTPException(status_code=400, detail="Student name is required.")
    if not student.email:
        raise HTTPException(status_code=400, detail="Student email is required.")
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Include email in response
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Include email in response