'''
Defines the API routes for the application, including student and course management.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from pydantic import BaseModel
# Pydantic model for Course request validation
class CourseCreate(BaseModel):
    name: str
    level: str
class StudentCreate(BaseModel):
    name: str
    email: str
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Creates a new student.
    '''
    new_student = Student(name=student.name, email=student.email)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"id": new_student.id, "name": new_student.name, "email": new_student.email}
@router.get("/students/", response_model=list)
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieves all students.
    '''
    return db.query(Student).all()
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Creates a new course.
    '''
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"id": new_course.id, "name": new_course.name, "level": new_course.level}
@router.get("/courses/", response_model=list)
def get_courses(db: Session = Depends(get_db)):
    '''
    Retrieves all courses.
    '''
    return db.query(Course).all()
@router.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    '''
    Enrolls a student in a course.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully"}