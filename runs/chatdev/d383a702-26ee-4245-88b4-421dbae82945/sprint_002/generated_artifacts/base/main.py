'''
Creates a FastAPI application for managing students.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate, Student as StudentSchema
from database import engine, get_db
# Create the FastAPI application
app = FastAPI()
# Create the database tables
@app.on_event("startup")
def startup():
    # Create the database tables automatically on startup
    from database import Base
    Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentSchema)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentSchema])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students