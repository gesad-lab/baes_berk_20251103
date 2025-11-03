'''
API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student.
    '''
    try:
        db_student = Student(name=student.name, email=student.email)  # Include email in Student creation
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email)  # Return StudentResponse instance
    except Exception as e:
        db.rollback()  # Rollback the session in case of error
        raise HTTPException(status_code=400, detail=str(e))  # Return an error response
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieve all students.
    '''
    students = db.query(Student).all()
    return [StudentResponse(id=student.id, name=student.name, email=student.email) for student in students]
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course.
    '''
    try:
        db_course = Course(name=course.name, level=course.level)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return CourseResponse(id=db_course.id, name=db_course.name, level=db_course.level)  # Return CourseResponse instance
    except Exception as e:
        db.rollback()  # Rollback the session in case of error
        raise HTTPException(status_code=400, detail=str(e))  # Return an error response