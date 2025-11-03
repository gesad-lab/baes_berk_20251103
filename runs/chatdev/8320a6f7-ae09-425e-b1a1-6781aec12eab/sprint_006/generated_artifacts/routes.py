'''
Defines the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel, Teacher as TeacherModel
from database import get_db
from pydantic import BaseModel
# Pydantic models for request validation
class Student(BaseModel):
    name: str
    email: str
    course_ids: list[int] = []
class Course(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added teacher_id to associate with Teacher
class Teacher(BaseModel):
    name: str
    email: str
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: list[Course] = []
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
    teacher_id: int  # Added teacher_id to response
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: Student, db: Session = Depends(get_db)):
    db_student = StudentModel(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    for course_id in student.course_ids:
        course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
        if course:
            db_student.courses.append(course)
        else:
            raise HTTPException(status_code=400, detail=f"Course with ID {course_id} does not exist.")
    db.commit()
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email, "courses": db_student.courses}
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(StudentModel).all()
    return [{"id": student.id, "name": student.name, "email": student.email, "courses": student.courses} for student in students]
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: Course, db: Session = Depends(get_db)):
    db_course = CourseModel(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Updated to include teacher_id
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level, "teacher_id": db_course.teacher_id}
@router.get("/courses/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    db_teacher = TeacherModel(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    teachers = db.query(TeacherModel).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]