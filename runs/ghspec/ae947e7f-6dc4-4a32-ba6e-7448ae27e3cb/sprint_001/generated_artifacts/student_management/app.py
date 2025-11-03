from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "sqlite:///./students.db"  # SQLite database file

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Define a base class for SQLAlchemy models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Required field

# Create the FastAPI app
app = FastAPI()

# Pydantic model for request body
class StudentCreate(BaseModel):
    name: str

def create_student_table():
    """
    Creates the SQLite database and the students table on startup.
    Will only execute if the tables do not already exist.
    """
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    """
    Handler for the startup event. It is executed when the application starts.
    """
    create_student_table()  # Initialize the database and create tables

@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate):
    """
    Create a new student in the database.

    - **student**: The student information to create (name is required).
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    new_student = Student(name=student.name)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    session.close()
    return new_student

@app.get("/students/{student_id}", response_model=StudentCreate)
def read_student(student_id: int):
    """
    Retrieve a student by ID from the database.

    - **student_id**: The ID of the student to retrieve.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()
    session.close()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student