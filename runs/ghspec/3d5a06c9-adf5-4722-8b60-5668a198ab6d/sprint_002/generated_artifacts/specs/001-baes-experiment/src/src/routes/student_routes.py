```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student  # Assuming a Student model exists with an email field
from src.schemas import StudentCreate, StudentResponse  # Assuming these schemas are defined

router = APIRouter()

@router.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    # Validate required email field
    if not student.email:
        raise HTTPException(status_code=400, detail="E001: Email field is required.")

    new_student = Student(name=student.name, email=student.email)
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.get("/students/{student_id}", response_model=StudentResponse)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found.")
    
    return student

@router.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    # Validate required email field
    if not student.email:
        raise HTTPException(status_code=400, detail="E001: Email field is required.")

    db_student = db.query(Student).filter(Student.id == student_id).first()
    
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found.")

    db_student.name = student.name
    db_student.email = student.email

    db.commit()
    db.refresh(db_student)

    return db_student

@router.get("/students", response_model=list[StudentResponse])
async def list_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students
```