'''
Main entry point for the application.
'''
# Import necessary modules
from fastapi import FastAPI, Depends
from database import init_db, get_db, migrate_db
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
from sqlalchemy.orm import Session
app = FastAPI()
@app.on_event("startup")
def startup_event():
    '''
    Initialize the database on startup.
    '''
    init_db()
    migrate_db()  # Ensure migration is called on startup
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Assign courses to the student
    if student.course_ids:
        courses = db.query(Course).filter(Course.id.in_(student.course_ids)).all()
        db_student.courses.extend(courses)
        db.commit()
    return db_student
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    '''
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
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