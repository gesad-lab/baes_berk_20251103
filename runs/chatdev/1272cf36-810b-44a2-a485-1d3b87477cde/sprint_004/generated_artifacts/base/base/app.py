'''
Main FastAPI application for the Student entity.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import init_db, get_db
from schemas import StudentCreate, StudentResponse
app = FastAPI()
# Initialize the database
init_db()
@app.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    db_student = Student(name=student.name, email=student.email)  # Handle email field
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return students