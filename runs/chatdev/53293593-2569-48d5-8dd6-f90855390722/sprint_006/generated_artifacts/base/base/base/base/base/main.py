'''
Implements the FastAPI application for managing Student entities.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Database
from models import Student
from schemas import StudentSchema
app = FastAPI()
database = Database()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    database.create_database()
@app.post("/students/", response_model=StudentSchema)
def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/{student_id}", response_model=StudentSchema)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student