```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.student import Student
from schemas.student_schemas import StudentCreate, StudentResponse
from db.database import get_db

router = APIRouter()

# Create a new student
@router.post("/students/", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate, db: Session = next(get_db())):
    new_student = Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Retrieve a student by ID
@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = next(get_db())):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update a student's name by ID
@router.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, student: StudentCreate, db: Session = next(get_db())):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db_student.name = student.name
    db.commit()
    return db_student

# Delete a student by ID
@router.delete("/students/{student_id}", status_code=200)
async def delete_student(student_id: int, db: Session = next(get_db())):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"detail": "Student deleted successfully"}
```