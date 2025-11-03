```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, constr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models.student import Student  # Importing the Student model from models

DATABASE_URL = "sqlite:///./students.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

class StudentCreate(BaseModel):
    """Schema for student creation."""
    name: constr(strip_whitespace=True, min_length=1)
    email: EmailStr  # Validate email format using Pydantic

class StudentResponse(BaseModel):
    """Schema for student response."""
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate):
    """Create a new student."""
    db = SessionLocal()
    new_student = Student(name=student.name, email=student.email)  # Create Student object

    db.add(new_student)
    try:
        db.commit()  # Commit the transaction to the database
        db.refresh(new_student)  # Refresh the instance with data from the database
    except IntegrityError:
        db.rollback()  # Rollback the session in case of an error
        raise HTTPException(status_code=400, detail="Student could not be created.")
    finally:
        db.close()  # Ensure the session is closed after operation

    return new_student  # Return the newly created student

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int):
    """Retrieve a specific student's details."""
    db = SessionLocal()
    
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found.")
    
    db.close()  # Close database session
    return student  # Return the found student
```