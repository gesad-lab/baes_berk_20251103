```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from uuid import uuid4
from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from .database import SessionLocal, engine

app = FastAPI()
Base = declarative_base()

# Define the Teacher model with appropriate fields
class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)

# Pydantic model for validating teacher inputs
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

# Endpoint for creating a new teacher
@app.post("/teachers", response_model=TeacherCreate, status_code=201)
def create_teacher(teacher: TeacherCreate):
    db: Session = SessionLocal()
    # Check for missing fields
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Missing required fields"}})
    
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    db.close()
    return db_teacher

# Endpoint for retrieving a teacher by ID
@app.get("/teachers/{teacher_id}", response_model=TeacherCreate)
def get_teacher(teacher_id: int):
    db: Session = SessionLocal()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    db.close()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# Endpoint for retrieving all teachers
@app.get("/teachers", response_model=List[TeacherCreate])
def list_teachers():
    db: Session = SessionLocal()
    teachers = db.query(Teacher).all()
    db.close()
    return teachers
```