# src/api/teachers.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.teacher import Teacher

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str  # Teacher's name is required and must be a string
    email: EmailStr  # Teacher's email is required and must be a valid email format

@router.post("/teachers")
def create_teacher(teacher: TeacherCreate):
    """Create a new teacher in the system."""
    db = SessionLocal()
    
    # Check for existing teacher with the same email
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Email already exists"}})
    
    # Validate the name field
    if not teacher.name.strip():
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Name is required"}})

    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    
    db.add(new_teacher)  # Add the new teacher to the session
    db.commit()  # Commit the transaction to save the new teacher
    db.refresh(new_teacher)  # Refresh the instance to get the new state

    return {
        "message": "Teacher created successfully",
        "teacher": {
            "name": new_teacher.name,
            "email": new_teacher.email
        }
    }

@router.get("/teachers")
def get_teachers():
    """Retrieve all the teachers from the system."""
    db = SessionLocal()
    teachers = db.query(Teacher).all()  # Retrieve all teachers
    
    return {
        "teachers": [{"name": teacher.name, "email": teacher.email} for teacher in teachers]
    }