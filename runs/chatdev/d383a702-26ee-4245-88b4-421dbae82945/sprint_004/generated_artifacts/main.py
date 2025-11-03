'''
Creates a FastAPI application for managing students and courses.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course  # Ensure these are imported
from schemas import StudentCreate, Student as StudentSchema, CourseCreate, Course as CourseSchema
from database import engine, get_db
# Create the FastAPI application
app = FastAPI()
# Create the database tables
@app.on_event("startup")
def startup():
    from database import Base
    Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentSchema)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentSchema])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@app.post("/courses/", response_model=CourseSchema)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/", response_model=list[CourseSchema])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@app.post("/students/{student_id}/courses/{course_id}")
def add_course_to_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Adds a course to a student. If the student or course does not exist, raises a 404 error.
    If the course is already associated with the student, raises a 400 error.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    # Check if the course is already associated with the student
    if course in student.courses:
        raise HTTPException(status_code=400, detail="Course already associated with the student")
    student.courses.append(course)
    db.commit()
    return student