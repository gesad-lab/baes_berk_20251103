from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from . import models, database

router = APIRouter()

# Pydantic models for request and response schemas
class StudentCreate(BaseModel):
    name: str = Field(..., example="John Doe", description="Name of the student")

class StudentResponse(BaseModel):
    id: int
    name: str

@router.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: Session = database.get_db()):
    # Validate student name
    if not student.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name field is required."}})

    # Create a new student entry
    new_student = models.Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    # Return the created student details
    return StudentResponse(id=new_student.id, name=new_student.name)

@router.get("/students/{id}", response_model=StudentResponse)
async def read_student(id: int, db: Session = database.get_db()):
    # Retrieve the student by ID
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Student not found."}})

    # Return the found student details
    return StudentResponse(id=student.id, name=student.name)