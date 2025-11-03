from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import os

# Configure SQLite database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")

# Initialize database connection and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create database tables on startup
def init_db():
    Base.metadata.create_all(bind=engine)

# Pydantic model for student creation
class StudentCreate(BaseModel):
    name: str

# FastAPI instance
app = FastAPI()

# Initialize the database
init_db()

@app.post("/students", response_model=StudentCreate, status_code=201)
def create_student(student: StudentCreate):
    """
    Create a new student in the database.

    :param student: StudentCreate object containing the student's name.
    :return: The created student object.
    """
    if not student.name:
        raise HTTPException(status_code=400, detail="The 'name' field must be a non-empty string.")
    
    db = SessionLocal()
    new_student = Student(name=student.name)
    db.add(new_student)
    try:
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Student creation failed due to a database error.")
    finally:
        db.close()

    return new_student

@app.get("/students", response_model=list[StudentCreate], status_code=200)
def get_students():
    """
    Retrieve all students from the database.

    :return: List of student objects.
    """
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()

    return students