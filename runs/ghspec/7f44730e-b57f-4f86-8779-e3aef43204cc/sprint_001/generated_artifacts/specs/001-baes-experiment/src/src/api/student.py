```python
# src/api/student.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal, init_db
from models.student import Student

app = FastAPI()

class StudentCreate(BaseModel):
    name: str

@app.post("/students")
def create_student(student: StudentCreate):
    """Create a new student record.

    Args:
        student (StudentCreate): The student information including 'name'.

    Raises:
        HTTPException: Raised if the name is missing.

    Returns:
        dict: A success message and the created student information.
    """
    if not student.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name is required"}})

    db = SessionLocal()
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message": "Student created successfully", "student": {"name": db_student.name}}

@app.get("/students")
def get_students():
    """Retrieve a list of all student records.

    Returns:
        dict: A list of students.
    """
    db = SessionLocal()
    students = db.query(Student).all()
    
    # Structure the student list to return only names
    return {"students": [{"name": student.name} for student in students]}

# Initialize the database on application startup
@app.on_event("startup")
def startup():
    """Initialize the database schema."""
    init_db()
```