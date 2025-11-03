```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Base model for SQLAlchemy
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Pydantic model for request/response
class StudentCreate(BaseModel):
    name: str = Field(..., description="The name of the student")

class StudentResponse(BaseModel):
    id: int
    name: str

# FastAPI application
app = FastAPI()

# Database settings
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database schema
def initialize_database():
    Base.metadata.create_all(bind=engine)

# Create a new student
@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    with SessionLocal() as session:
        db_student = Student(name=student.name)
        session.add(db_student)
        session.commit()
        session.refresh(db_student)  # Refresh the instance to get the id
        return db_student

# Retrieve a student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    with SessionLocal() as session:
        student = session.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Student not found."}})
        return student

# Initialize the database on application startup
@app.on_event("startup")
def startup_event():
    initialize_database()
```