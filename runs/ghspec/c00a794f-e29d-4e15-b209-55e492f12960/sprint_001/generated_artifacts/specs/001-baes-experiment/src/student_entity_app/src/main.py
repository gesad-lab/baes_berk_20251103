```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from typing import List

# Database Setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Model Definition
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)  # Name must be provided

# Create the database schema
Base.metadata.create_all(bind=engine)

# FastAPI Instance
app = FastAPI()


# Pydantic Schema for Student Input
class StudentCreate(BaseModel):
    name: str  # Name of the student


# Pydantic Schema for Returning Student
class StudentRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a new student
@app.post("/students/", response_model=StudentRead)
async def create_student(student: StudentCreate, db: SessionLocal = next(get_db())):
    new_student = Student(name=student.name)
    db.add(new_student)
    try:
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Student with this name already exists.")
    return new_student


# Get all students
@app.get("/students/", response_model=List[StudentRead])
async def read_students(skip: int = 0, limit: int = 100, db: SessionLocal = next(get_db())):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students


# Error Handling for missing name
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": "E001", "message": exc.detail}},
    )
```