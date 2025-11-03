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
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: Optional[int]  # Made teacher_id optional to handle cases where it may not be provided
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: Optional[int]  # Made teacher_id optional in the response model
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
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Endpoint to create a new course with an associated teacher.
    '''
    # Validate that the teacher_id exists if provided
    if course.teacher_id is not None and not db.query(Teacher).filter(Teacher.id == course.teacher_id).first():
        raise HTTPException(status_code=400, detail="Teacher ID does not exist.")
    new_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {
        "id": new_course.id,
        "name": new_course.name,
        "level": new_course.level,
        "teacher_id": new_course.teacher_id
    }