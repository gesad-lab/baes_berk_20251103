'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from models import Base, Student
from database import engine
from schemas import StudentCreate, StudentResponse
from sqlalchemy.orm import Session
app = FastAPI()
# Create the database tables
Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db: Session = Session(bind=engine)
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student