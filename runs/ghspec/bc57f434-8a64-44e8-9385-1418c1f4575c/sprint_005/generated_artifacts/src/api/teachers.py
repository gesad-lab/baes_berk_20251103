from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Teacher  # Importing existing Teacher model
from pydantic import BaseModel, EmailStr

router = APIRouter()

class TeacherResponse(BaseModel):
    """Response model for returning teacher information."""
    id: int
    name: str
    email: EmailStr

class TeacherCreate(BaseModel):
    """Request model for creating a new teacher."""
    name: str
    email: EmailStr

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """Create a new teacher entry."""
    # Check for existing email before adding a new teacher
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=409, detail={"error": {"code": "E002", "message": "Email already exists."}})
    
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Retrieve a teacher's details by their ID."""
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Teacher not found."}})
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)