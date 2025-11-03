'''
Contains the API endpoints for managing Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher  # Import Teacher model
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
class CourseCreate(BaseModel):
    name: str
    level: str
class TeacherCreate(BaseModel):  # New model for Teacher
    name: str
    email: EmailStr  # Email field with validation
class StudentCoursesUpdate(BaseModel):  # Defined StudentCoursesUpdate model
    course_ids: list[int]  # Assuming course_ids is a list of integers
router = APIRouter()
@router.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentCreate(name=db_student.name, email=db_student.email)
@router.get("/students/", response_model=list[StudentCreate])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return [StudentCreate(name=student.name, email=student.email) for student in students]
@router.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return CourseCreate(name=db_course.name, level=db_course.level)
@router.get("/courses/", response_model=list[CourseCreate])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return [CourseCreate(name=course.name, level=course.level) for course in courses]
@router.post("/teachers/", response_model=TeacherCreate)  # New endpoint for creating Teacher
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return TeacherCreate(name=db_teacher.name, email=db_teacher.email)
@router.get("/teachers/", response_model=list[TeacherCreate])  # New endpoint for getting Teachers
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(Teacher).all()
    return [TeacherCreate(name=teacher.name, email=teacher.email) for teacher in teachers]
@router.put("/students/{student_id}/courses/", response_model=StudentCreate)
def add_courses_to_student(student_id: int, course_ids: StudentCoursesUpdate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    courses = db.query(Course).filter(Course.id.in_(course_ids.course_ids)).all()
    for course in courses:
        if course not in db_student.courses:
            db_student.courses.append(course)
    db.commit()
    db.refresh(db_student)
    return StudentCreate(name=db_student.name, email=db_student.email)