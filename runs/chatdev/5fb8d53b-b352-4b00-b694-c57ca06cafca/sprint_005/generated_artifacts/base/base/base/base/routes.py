'''
Defines the API endpoints for CRUD operations on the Student entity.
'''
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student
from database import SessionLocal
student_router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@student_router.post("/students/", response_model=dict)
async def create_student(name: str, db: Session = Depends(get_db)):
    '''
    Creates a new student with the provided name.
    '''
    student = Student(name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name}
@student_router.get("/students/{student_id}", response_model=dict)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    '''
    Retrieves a student by ID.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student.id, "name": student.name}