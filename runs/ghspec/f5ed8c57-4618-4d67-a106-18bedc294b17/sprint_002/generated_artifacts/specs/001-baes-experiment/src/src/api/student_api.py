```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.database import get_db, Student  # Importing the Student model and database access method

router = APIRouter()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Using Pydantic for email validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Assuming Student model has name and email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/students", response_model=list[StudentResponse])
async def list_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students
```