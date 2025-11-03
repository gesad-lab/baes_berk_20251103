'''
Contains the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import get_db
from pydantic import BaseModel
from typing import List, Optional
router = APIRouter()
class TeacherCreate(BaseModel):
    name: str
    email: str
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new teacher.
    '''
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return {
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }
@router.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    '''
    Endpoint to retrieve all teachers.
    '''
    return [{
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    } for teacher in db.query(Teacher).all()]