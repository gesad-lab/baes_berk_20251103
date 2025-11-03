from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///./test.db"

# Initialize the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()

# SQLAlchemy Student model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Pydantic schema for creating and returning Student objects
class StudentCreate(BaseModel):
    name: str

class StudentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Initialize the FastAPI app
app = FastAPI()

# Create the database schema on startup
@app.on_event("startup")
def startup():
    # Create the database tables
    Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new student
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Retrieve a student's details by name
@app.get("/students/{student_name}", response_model=StudentResponse)
def read_student(student_name: str, db: Session = next(get_db())):
    student = db.query(Student).filter(Student.name == student_name).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update a student's name
@app.put("/students/{student_name}", response_model=StudentResponse)
def update_student(student_name: str, new_student: StudentCreate, db: Session = next(get_db())):
    student = db.query(Student).filter(Student.name == student_name).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = new_student.name
    db.commit()
    db.refresh(student)
    return student

# Delete a student by name
@app.delete("/students/{student_name}", response_model=dict)
def delete_student(student_name: str, db: Session = next(get_db())):
    student = db.query(Student).filter(Student.name == student_name).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"detail": "Student deleted successfully"}