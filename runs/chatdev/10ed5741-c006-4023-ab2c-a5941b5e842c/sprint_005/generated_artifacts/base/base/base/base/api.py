'''
Contains the API endpoints for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from pydantic import BaseModel
router = APIRouter()
class StudentCreate(BaseModel):
    name: str
class StudentResponse(BaseModel):
    id: int
    name: str
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new student.
    '''
    new_student = Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id, "name": new_student.name}
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all students.
    '''
    return [{"id": student.id, "name": student.name} for student in db.query(Student).all()]