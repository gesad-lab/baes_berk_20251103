'''
Router for handling student-related API endpoints.
'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import StudentCreate, StudentResponse
from crud import create_student, get_students, add_course_to_student, get_student_courses
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)
@router.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)
@router.post("/students/{student_id}/courses/{course_id}/")
def assign_course_to_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    return add_course_to_student(db=db, student_id=student_id, course_id=course_id)
@router.get("/students/{student_id}/courses/")
def read_student_courses(student_id: int, db: Session = Depends(get_db)):
    return get_student_courses(db=db, student_id=student_id)