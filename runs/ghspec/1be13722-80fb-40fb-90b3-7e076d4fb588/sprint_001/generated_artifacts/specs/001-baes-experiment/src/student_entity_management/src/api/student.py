from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Pydantic model for request validation
class StudentCreate(BaseModel):
    name: str = Field(..., title="The name of the student", max_length=100)

# Create a student endpoint
@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate):
    # Validate that the name is provided
    if not student.name:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Name is required."
                }
            }
        )
    
    # Create a new student record
    db = SessionLocal()
    db_student = Student(name=student.name)
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    
    return {"id": db_student.id, "name": db_student.name}

# Retrieve students endpoint
@app.get("/students", response_model=List[StudentCreate])
def read_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students