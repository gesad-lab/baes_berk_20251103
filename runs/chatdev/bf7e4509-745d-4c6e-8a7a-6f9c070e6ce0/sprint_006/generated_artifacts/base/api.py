'''
Contains the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel, Teacher as TeacherModel  # Import Teacher model
from database import get_db
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation
# Pydantic model for Student request validation
class Student(BaseModel):
    name: str
    email: EmailStr  # Added email field with validation
    course_ids: list[int] = []  # Add this line to include course IDs
# Pydantic model for Course request validation
class Course(BaseModel):
    name: str
    level: str
# Pydantic model for Teacher request validation
class Teacher(BaseModel):
    name: str
    email: EmailStr
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Enroll in courses if provided
    for course_id in student.course_ids:
        course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
        if course:
            db_student.courses.append(course)
    db.commit()
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email, "course_ids": student.course_ids}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [
        {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "course_ids": [course.id for course in student.courses]  # Include course IDs
        } for student in students
    ]
@router.post("/courses/", response_model=dict)
def create_course(course: Course, db: Session = Depends(get_db)):
    db_course = CourseModel(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    courses = db.query(CourseModel).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
@router.post("/students/{student_id}/courses/{course_id}/enroll")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": f"Student {student_id} enrolled in Course {course_id}"}
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    db_teacher = TeacherModel(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/teachers/", response_model=list)
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teachers = db.query(TeacherModel).offset(skip).limit(limit).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]