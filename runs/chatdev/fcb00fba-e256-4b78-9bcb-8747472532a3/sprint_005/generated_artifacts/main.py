'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
from fastapi.middleware.cors import CORSMiddleware
# Create the FastAPI app
app = FastAPI()
# Allow CORS for the Tkinter app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create the database tables
Student.metadata.create_all(bind=engine)
Course.metadata.create_all(bind=engine)
Teacher.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return students
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/", response_model=list[CourseResponse])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of courses from the database.
    '''
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Create a new teacher in the database.
    '''
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@app.get("/teachers/", response_model=list[TeacherResponse])
def read_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of teachers from the database.
    '''
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers
@app.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    '''
    Enroll a student in a course.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully"}