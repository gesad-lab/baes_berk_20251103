'''
Defines the API endpoints for CRUD operations on the Student and Course entities.
'''
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course
from database import SessionLocal
student_router = APIRouter()
course_router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@student_router.post("/students/", response_model=dict)
async def create_student(name: str, email: str, db: Session = Depends(get_db)):
    '''
    Creates a new student with the provided name and email.
    '''
    student = Student(name=name, email=email)  # Include email in student creation
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"id": student.id, "name": student.name, "email": student.email}
@student_router.get("/students/{student_id}", response_model=dict)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    '''
    Retrieves a student by ID.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": student.id, "name": student.name, "email": student.email}  # Include email in response
@course_router.post("/courses/", response_model=dict)
async def create_course(name: str, level: str, db: Session = Depends(get_db)):
    '''
    Creates a new course with the provided name and level.
    '''
    course = Course(name=name, level=level)
    db.add(course)
    db.commit()
    db.refresh(course)
    return {"id": course.id, "name": course.name, "level": course.level}
@course_router.get("/courses/{course_id}", response_model=dict)
async def read_course(course_id: int, db: Session = Depends(get_db)):
    '''
    Retrieves a course by ID.
    '''
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"id": course.id, "name": course.name, "level": course.level}