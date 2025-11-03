'''
Defines the API routes for the Student and Course entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_student, get_students, create_course, get_courses
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
router = APIRouter()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/students/", response_model=StudentResponse)
def add_student(student: StudentCreate, course_ids: list[int] = None, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    if course_ids:
        # Fetch existing courses based on provided course_ids
        existing_courses = db.query(Course).filter(Course.id.in_(course_ids)).all()
        if not existing_courses:
            raise HTTPException(status_code=400, detail="No valid courses found for the provided course IDs.")
        db_student.courses = existing_courses
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@router.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)
@router.post("/courses/", response_model=CourseResponse)
def add_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)
@router.get("/courses/", response_model=list[CourseResponse])
def read_courses(db: Session = Depends(get_db)):
    return get_courses(db=db)