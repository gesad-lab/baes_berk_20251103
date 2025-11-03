from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from models import Student, Base  # Assuming Student model includes necessary fields
from database import get_db  # Adjust import according to your project structure

app = FastAPI()

class StudentCreateModel(BaseModel):
    name: str
    email: EmailStr  # Automatically validates email format

@app.post("/students", response_model=Student)
async def create_student(student: StudentCreateModel, db: Session = Depends(get_db)):
    """
    Create a new student with the provided name and email.
    
    Parameters:
    - student: StudentCreateModel containing the student's name and email.
    - db: Database session.

    Returns:
    - The created Student object.
    
    Raises:
    - HTTPException: If email is missing or invalid (handled by Pydantic).
    """
    # Create a new Student instance
    new_student = Student(name=student.name, email=student.email)
    
    # Add the new student to the database session
    db.add(new_student)
    try:
        db.commit()  # Commit the transaction
        db.refresh(new_student)  # Refresh to get the latest data (e.g. ID)
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=str(e))
    
    return new_student

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a student by their ID.
    
    Parameters:
    - student_id: The ID of the student to retrieve.
    - db: Database session.

    Returns:
    - The Student object if found.
    
    Raises:
    - HTTPException: If the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student