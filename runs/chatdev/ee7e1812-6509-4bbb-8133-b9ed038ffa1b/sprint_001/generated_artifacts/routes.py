'''
Contains the API endpoints for the Student entity.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from schemas import StudentCreate  # Import the Pydantic model
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Creates a new student in the database.
    '''
    try:
        db_student = Student(name=student.name)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return {"id": db_student.id, "name": db_student.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieves a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name} for student in students]