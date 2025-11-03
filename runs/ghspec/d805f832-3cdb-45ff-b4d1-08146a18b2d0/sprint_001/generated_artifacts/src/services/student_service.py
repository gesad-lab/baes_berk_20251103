```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# SQLAlchemy base class
Base = declarative_base()

# Database connection string
DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy engine and session configuration
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Student model definition
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# FastAPI app instance
app = FastAPI()

# Pydantic model for student creation
class StudentCreate(BaseModel):
    name: str

# Pydantic model for student retrieval
class StudentOut(BaseModel):
    id: int
    name: str

# Create the SQLite database schema
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new student
@app.post("/students", response_model=StudentOut, status_code=201)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """
    Create a new student.
    
    Args:
        student (StudentCreate): The student data to create.
        db (Session): The database session.

    Returns:
        StudentOut: The created student information.
        
    Raises:
        HTTPException: If the student cannot be created.
    """
    if not student.name:
        raise HTTPException(status_code=400, detail={"code": "E001", "message": "Name is required."})

    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Retrieve a student by ID
@app.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = next(get_db())):
    """
    Retrieve student details by ID.
    
    Args:
        student_id (int): The ID of the student to retrieve.
        db (Session): The database session.

    Returns:
        StudentOut: The student information.
        
    Raises:
        HTTPException: If the student is not found.
    """
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail={"code": "E002", "message": "Student not found."})

    return db_student
```