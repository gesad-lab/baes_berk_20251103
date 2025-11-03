'''
Contains the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import SessionLocal
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
student_router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@student_router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@student_router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
@student_router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@student_router.post("/students/{student_id}/courses/", response_model=CourseResponse)
def enroll_student_in_course(student_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_course = db.query(Course).filter(Course.name == course.name, Course.level == course.level).first()
    if db_course is None:
        db_course = Course(name=course.name, level=course.level)
        db.add(db_course)
    db_student.courses.append(db_course)  # Add course to student's courses
    db.commit()  # Commit the changes to the database
    db.refresh(db_student)  # Refresh the student instance
    return db_course
@student_router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@student_router.put("/courses/{course_id}/assign_teacher/{teacher_id}", response_model=CourseResponse)
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_course.teacher_id = teacher_id  # Assign teacher to course
    db.commit()
    db.refresh(db_course)
    return db_course