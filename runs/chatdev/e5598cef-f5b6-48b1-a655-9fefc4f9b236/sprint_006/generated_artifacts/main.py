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
# Create the database tables if they do not exist
Base.metadata.create_all(bind=engine)
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    # Check if the teacher exists
    if course.teacher_id is not None:
        teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Include teacher_id
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/", response_model=list[CourseResponse])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@app.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    # Check if the student is already enrolled in the course
    if course in student.courses:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course")
    student.courses.append(course)
    db.commit()
    return {"msg": "Student enrolled in course successfully"}
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    # Check if a teacher with the same email already exists
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Teacher with this email already exists")
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@app.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers