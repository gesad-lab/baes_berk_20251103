from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema
Base.metadata.create_all(bind=engine)

# FastAPI application instance
app = FastAPI()

# Pydantic model for request validation
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the student")

# API endpoint to create a new student
@app.post("/students", response_model=StudentCreate, status_code=201)
def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    new_student = Student(name=student.name)
    db.add(new_student)

    try:
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Name must not be empty.")
    finally:
        db.close()
    
    return JSONResponse(content={"id": new_student.id, "name": new_student.name}, status_code=201)

# API endpoint to get a specific student
@app.get("/students/{student_id}", response_model=StudentCreate)
def read_student(student_id: int):
    db: Session = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.close()

    return JSONResponse(content={"id": student.id, "name": student.name})