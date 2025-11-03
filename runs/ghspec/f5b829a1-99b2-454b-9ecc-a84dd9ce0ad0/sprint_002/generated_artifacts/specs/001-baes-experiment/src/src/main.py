```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models import Student
from src.database import get_db

app = FastAPI()

# Create student endpoint
@app.post("/students", response_model=Student, status_code=201)
async def create_student(name: str, email: str, db: Session = Depends(get_db)):
    """
    Create a new student with a name and email.

    Args:
        name (str): The name of the student.
        email (str): The email of the student.

    Returns:
        Student: The created student with ID, name, and email.
    
    Raises:
        HTTPException: If name or email is missing or invalid.
    """
    if not name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email field is required.")
    
    db_student = Student(name=name, email=email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Retrieve student endpoint
@app.get("/students/{student_id}", response_model=Student)
async def retrieve_student(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a student by their ID.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        Student: The retrieved student with ID, name, and email.
    
    Raises:
        HTTPException: If the student with the given ID does not exist.
    """
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    return db_student
```