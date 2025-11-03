'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from schemas import StudentCreate, StudentResponse
from sqlalchemy import create_engine
from models import Base
app = FastAPI()
# Database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students