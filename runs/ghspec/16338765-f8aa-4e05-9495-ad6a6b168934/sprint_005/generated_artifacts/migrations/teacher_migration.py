```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import List
from sqlalchemy.orm import Session
from src.database import get_db  # Assumed database session management
from src.models import Teacher  # Assumed teacher model is defined

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherUpdate(BaseModel):
    name: str = None
    email: EmailStr = None

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

@router.post("/teachers", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, updates: TeacherUpdate, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    # Only update fields that are provided
    if updates.name is not None:
        teacher.name = updates.name
    if updates.email is not None:
        teacher.email = updates.email
    
    db.commit()
    db.refresh(teacher)
    return teacher
```