'''
API routes for the Student and Course entities.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import create_database, get_db
from models import Student, Course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
app = FastAPI()
# Create the database on startup
@app.on_event("startup")
def startup():
    create_database()
@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student in the database.
    """
    db_student = Student(name=student.name, email=student.email)  # Added email to student creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of students from the database.
    """
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@app.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course in the database.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses", response_model=list[CourseResponse])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of courses from the database.
    """
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@app.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Enroll a student in a course.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course"}