'''
Main entry point of the FastAPI application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
# Create the FastAPI app
app = FastAPI()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if not student.name:
        raise HTTPException(status_code=400, detail="Student name is required")
    if not student.email:
        raise HTTPException(status_code=400, detail="Student email is required")
    db_student = Student(name=student.name, email=student.email)
    if student.course_ids:
        courses = db.query(Course).filter(Course.id.in_(student.course_ids)).all()
        db_student.courses.extend(courses)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email, courses=[CourseResponse.from_orm(course) for course in db_student.courses])
@app.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    if not course.name:
        raise HTTPException(status_code=400, detail="Course name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="Course level is required")
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return CourseResponse(id=db_course.id, name=db_course.name, level=db_course.level)
@app.get("/courses/", response_model=list[CourseResponse])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    if not teacher.name:
        raise HTTPException(status_code=400, detail="Teacher name is required")
    if not teacher.email:
        raise HTTPException(status_code=400, detail="Teacher email is required")
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return TeacherResponse(id=db_teacher.id, name=db_teacher.name, email=db_teacher.email)
@app.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers