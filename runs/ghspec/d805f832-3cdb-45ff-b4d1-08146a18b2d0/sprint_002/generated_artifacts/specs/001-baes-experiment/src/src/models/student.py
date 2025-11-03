```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy.orm import Session
from fastapi import HTTPException

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class StudentCreateModel(BaseModel):
    name: str
    email: EmailStr  # Automatically validates email

    @validator('email')
    def validate_email_format(cls, email):
        if not email:
            raise ValueError('Email must be provided')
        return email

def create_student(db: Session, student: StudentCreateModel):
    # Function to create a new student in the database
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    # Function to retrieve a student by ID
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
```