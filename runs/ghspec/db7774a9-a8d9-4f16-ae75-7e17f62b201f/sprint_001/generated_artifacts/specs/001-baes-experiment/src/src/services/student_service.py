```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.student import Student
from schemas.student import StudentCreate, StudentResponse
from database import get_db
from typing import List

router = APIRouter()

@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """Creates a new student record."""
    if not student.name:
        raise HTTPException(status_code=400, detail={"code": "E001", "message": "Name is required."})
    
    new_student = Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def retrieve_student(student_id: int, db: Session = Depends(get_db)):
    """Retrieves a student record by ID."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail={"code": "E002", "message": "Student not found."})
    return student

@router.get("/students", response_model=List[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    """Retrieves a list of all students."""
    students = db.query(Student).all()
    return students
```