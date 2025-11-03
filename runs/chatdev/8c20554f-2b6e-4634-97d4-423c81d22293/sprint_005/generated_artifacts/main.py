'''
Main application file for the FastAPI backend.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
from sqlalchemy import inspect
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    existing_student = db.query(Student).filter(Student.name == student.name).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this name already exists.")
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email, courses=[])
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
    return CourseResponse(id=db_course.id, name=db_course.name, level=db_course.level, students=[])
@app.get("/courses/", response_model=list[CourseResponse])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of courses from the database.
    '''
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses
@app.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    '''
    Enroll a student in a course.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found.")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully."}
@app.get("/students/{student_id}/courses", response_model=list[CourseResponse])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    '''
    Retrieve courses for a specific student.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return [CourseResponse(id=course.id, name=course.name, level=course.level, students=[]) for course in student.courses]
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Create a new teacher in the database.
    '''
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return TeacherResponse(id=db_teacher.id, name=db_teacher.name, email=db_teacher.email)
@app.get("/teachers/", response_model=list[TeacherResponse])
def read_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of teachers from the database.
    '''
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return teachers