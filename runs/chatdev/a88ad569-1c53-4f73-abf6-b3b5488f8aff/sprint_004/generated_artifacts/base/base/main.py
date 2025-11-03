'''
Main application entry point for the Student Management system.
'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, create_database
from models import Student
from schemas import StudentCreate, StudentResponse
app = FastAPI()
@app.on_event("startup")
def startup_event():
    create_database()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student