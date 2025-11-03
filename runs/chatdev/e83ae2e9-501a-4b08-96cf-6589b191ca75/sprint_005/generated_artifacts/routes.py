'''
Defines the API routes for the Teacher entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Teacher  # Ensure Teacher model is imported
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
router = APIRouter()
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation
@router.post("/teachers/", response_model=TeacherCreate)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Create a new teacher in the database.
    '''
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@router.get("/teachers/", response_model=list[TeacherCreate])
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of teachers from the database.
    '''
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers