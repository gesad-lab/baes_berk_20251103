'''
Defines the API endpoints for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course
from database import get_db
from pydantic import BaseModel, EmailStr
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Add email field with validation
    course_ids: list[int] = []  # List of course IDs for enrollment
class CourseCreate(BaseModel):
    name: str
    level: str
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Enroll student in courses only if course_ids is not empty
    if student.course_ids:
        for course_id in student.course_ids:
            course = db.query(Course).filter(Course.id == course_id).first()
            if course:
                db_student.courses.append(course)
            else:
                raise HTTPException(status_code=404, detail=f"Course with id {course_id} not found.")
    db.commit()  # Commit changes after enrolling in courses
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]  # Include email