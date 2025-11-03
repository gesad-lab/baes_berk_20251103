```python
# src/routes/teacher_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, validator
from src.database.database import get_db
from src.models.teacher import Teacher  # Import Teacher model
from typing import List

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name must not be empty')
        return v

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Email already exists.")

    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

@router.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    return teacher

@router.get("/teachers/", response_model=List[TeacherResponse])
def list_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    return teachers
```