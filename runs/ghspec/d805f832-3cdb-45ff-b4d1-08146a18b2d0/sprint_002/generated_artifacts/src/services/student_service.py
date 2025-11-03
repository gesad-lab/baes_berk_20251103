```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.orm import Session
from models import Student, Base  # Assuming Student model is defined in models.py
from database import get_db  # Assuming get_db is defined for getting a session

app = FastAPI()

class StudentCreateModel(BaseModel):
    name: str
    email: EmailStr  # Automatically validates email format

@app.post("/students", response_model=Student, status_code=201)
async def create_student(student: StudentCreateModel, db: Session = Depends(get_db)):
    """
    Create a new Student with name and email.
    
    :param student: The student data including name and email.
    :param db: The database session dependency.
    :return: The created student object.
    :raises HTTPException: If the email is missing or invalid.
    """
    
    # Validate presence of email - handled by Pydantic's EmailStr
    try:
        student_data = Student(
            name=student.name,
            email=student.email
        )
        db.add(student_data)
        db.commit()
        db.refresh(student_data)
        return student_data
    except Exception as e:
        # Log exception (not shown here)
        db.rollback()  # Rollback in case of failure to avoid corruption
        raise HTTPException(status_code=400, detail="An error occurred while creating the student.") from e

# Example of retrieval logic (assuming it's implemented elsewhere)
@app.get("/students/{student_id}", response_model=Student)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a student by ID.

    :param student_id: The ID of the student to retrieve.
    :param db: The database session dependency.
    :return: The student object.
    :raises HTTPException: If student with the given ID does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
```