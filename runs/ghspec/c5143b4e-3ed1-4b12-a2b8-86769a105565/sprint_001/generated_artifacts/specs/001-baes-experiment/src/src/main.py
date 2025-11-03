from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Initialize FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create database schema
Base.metadata.create_all(bind=engine)

# Pydantic model for Student
class StudentCreate(BaseModel):
    name: str = Field(..., example="John Doe")

class StudentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Dependency to create a new session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Error response model
class ErrorResponse(BaseModel):
    error: dict

# Create Student Endpoint
@app.post("/students", response_model=StudentResponse, responses={400: {"model": ErrorResponse}})
async def create_student(student: StudentCreate, db: Session = next(get_db())):
    if not student.name:  # Validate that name is not empty
        raise HTTPException(
            status_code=400,
            detail={"code": "E001", "message": "Name is required", "details": {}}
        )

    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Retrieve Students Endpoint
@app.get("/students", response_model=List[StudentResponse])
async def read_students(db: Session = next(get_db())):
    students = db.query(Student).all()
    return students