'''
API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import get_db
from schemas import StudentCreate, StudentResponse
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student.
    '''
    try:
        db_student = Student(name=student.name)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return StudentResponse(id=db_student.id, name=db_student.name)  # Return StudentResponse instance
    except Exception as e:
        db.rollback()  # Rollback the session in case of error
        raise HTTPException(status_code=400, detail=str(e))  # Return an error response
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieve all students.
    '''
    students = db.query(Student).all()
    return [StudentResponse(id=student.id, name=student.name) for student in students]