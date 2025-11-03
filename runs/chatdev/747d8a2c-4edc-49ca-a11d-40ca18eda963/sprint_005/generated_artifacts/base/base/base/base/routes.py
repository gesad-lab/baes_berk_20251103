'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from pydantic import BaseModel
# Pydantic model for request validation
class StudentCreate(BaseModel):
    name: str
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''Creates a new student.'''
    db_student = Student(name=student.name)
    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error adding student.")
    return {"id": db_student.id, "name": db_student.name}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''Retrieves all students.'''
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name} for student in students]