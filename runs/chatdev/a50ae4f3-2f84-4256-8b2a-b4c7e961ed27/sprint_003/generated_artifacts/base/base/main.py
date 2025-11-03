'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from schemas import StudentCreate, StudentResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        db_student = Student(name=student.name)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()  # Rollback the session in case of error
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    try:
        return db.query(Student).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching students")