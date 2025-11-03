'''
Main entry point of the FastAPI application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Student
from schemas import StudentCreate, StudentResponse
# Create the FastAPI app
app = FastAPI()
# Create the database tables
Base.metadata.create_all(bind=engine)
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students