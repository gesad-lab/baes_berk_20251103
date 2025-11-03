from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database setup
DATABASE_URL = "sqlite:///./test.db"  # Change path as needed
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model definition
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema
def init_db():
    Base.metadata.create_all(bind=engine)

# Pydantic model for student input/output
class StudentCreate(BaseModel):
    name: str

class StudentOut(BaseModel):
    id: int
    name: str

# FastAPI app initialization
app = FastAPI(on_startup=[init_db])  # Initialize the database on startup

@app.post("/students", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = next(SessionLocal())):
    """
    Create a new student.
    
    Args:
        student (StudentCreate): The student's information.
        db (Session): SQLAlchemy session.

    Returns:
        StudentOut: The created student's information.
    """
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{id}", response_model=StudentOut)
def get_student(id: int, db: Session = next(SessionLocal())):
    """
    Retrieve a student by their unique identifier.
    
    Args:
        id (int): The unique identifier for the student.
        db (Session): SQLAlchemy session.

    Returns:
        StudentOut: The student's information, or raises HTTPException if not found.
    """
    student = db.query(Student).filter(Student.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student