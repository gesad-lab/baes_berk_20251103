from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Pydantic model for Student
class Student(BaseModel):
    name: str

class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create the database schema at startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=Student)
async def create_student(student: Student, db: SessionLocal = next(get_db())):
    """
    Create a new student.
    
    Parameters:
    - student: Student object containing the new student's data.
    
    Returns:
    - The created student's data.
    
    Raises:
    - HTTPException: If name is missing or if any database error occurs.
    """
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    
    student_model = StudentModel(name=student.name)
    db.add(student_model)
    db.commit()
    db.refresh(student_model)
    return student_model

@app.get("/students/", response_model=List[Student])
async def list_students(db: SessionLocal = next(get_db())):
    """
    Retrieve a list of all students.
    
    Parameters:
    - None.
    
    Returns:
    - A list of student objects.
    """
    students = db.query(StudentModel).all()
    return students