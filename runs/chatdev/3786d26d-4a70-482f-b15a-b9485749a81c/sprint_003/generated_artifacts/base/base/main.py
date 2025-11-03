'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from database import engine, SessionLocal
from models import Base
from schemas import StudentCreate, StudentResponse
from sqlalchemy.orm import Session
# Create the FastAPI app
app = FastAPI()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# API endpoint to create a new student
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    from models import Student
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
# API endpoint to get all students
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    from models import Student
    students = db.query(Student).offset(skip).limit(limit).all()
    return students