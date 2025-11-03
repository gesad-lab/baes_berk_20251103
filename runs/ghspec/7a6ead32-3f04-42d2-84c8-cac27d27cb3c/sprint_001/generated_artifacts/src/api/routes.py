```python
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, constr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Assuming models are defined in models.py

app = FastAPI()

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Student creation and update request body models
class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Name is required and must be at least 1 character long

class StudentUpdate(BaseModel):
    name: constr(min_length=1)  # Name is required and must be at least 1 character long

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = next(get_db())):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentUpdate, db: Session = next(get_db())):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db_student.name = student.name
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{student_id}", response_model=dict)
def delete_student(student_id: int, db: Session = next(get_db())):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"detail": "Student deleted successfully"}

# Automatically create database schema on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
```