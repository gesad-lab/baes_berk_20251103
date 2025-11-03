'''
Defines the API routes for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel
from database import get_db
from pydantic import BaseModel
# Pydantic model for request validation
class Student(BaseModel):
    name: str
class StudentResponse(BaseModel):
    id: int
    name: str
student_router = APIRouter()
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name}
@student_router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name} for student in students]