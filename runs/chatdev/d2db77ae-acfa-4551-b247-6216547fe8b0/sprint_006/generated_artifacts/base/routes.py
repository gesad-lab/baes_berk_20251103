'''
Defines the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, StudentCreate, Course, CourseCreate, Teacher, TeacherCreate
from database import get_db
router = APIRouter()
# Existing student and course routes...
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher in the database.
    """
    if not teacher.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not teacher.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/teachers/", response_model=list)
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of teachers from the database.
    """
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]