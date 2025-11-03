'''
Defines the API routes for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from pydantic import BaseModel, constr
class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Ensure name is not empty
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name}
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()