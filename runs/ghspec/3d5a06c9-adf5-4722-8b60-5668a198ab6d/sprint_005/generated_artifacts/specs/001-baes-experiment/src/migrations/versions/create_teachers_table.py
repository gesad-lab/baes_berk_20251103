```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import List

Base = declarative_base()

# Define the Teacher model corresponding to the new table
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# FastAPI application instance
app = FastAPI()

# Pydantic schema for Teacher response
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

# Dependency to get the database session
def get_db():
    # Assuming there's a function in a separate db module for session management
    from db import get_db_session
    db: Session = get_db_session()
    try:
        yield db
    finally:
        db.close()

@app.post("/teachers", response_model=TeacherResponse, status_code=201)
async def create_teacher(teacher: TeacherResponse, db: Session = Depends(get_db)):
    # Validate input and create a new Teacher
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Both name and email are required"}})

    # Check for existing email
    if db.query(Teacher).filter(Teacher.email == teacher.email).first():
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email is already registered"}})

    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

# Migration script to create the teachers table
def create_teachers_table():
    from db import engine
    Base.metadata.create_all(bind=engine)
```