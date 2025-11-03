'''
Main application file for the Student API using FastAPI.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import engine, get_db
from schemas import StudentCreate, StudentResponse
# Create FastAPI instance
app = FastAPI()
# Create the database tables on startup
@app.on_event("startup")
def startup():
    from database import Base
    Base.metadata.create_all(bind=engine)
# Endpoint to create a new student
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
# Endpoint to get all students
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students