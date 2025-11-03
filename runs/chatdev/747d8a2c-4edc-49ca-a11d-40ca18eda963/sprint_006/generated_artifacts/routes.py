'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import get_db
from pydantic import BaseModel
# Pydantic models for request validation
class StudentCreate(BaseModel):
    name: str
    email: str  # Added email field
class CourseCreate(BaseModel):
    name: str
    level: str
    teacher_id: int  # Added teacher_id field
class TeacherCreate(BaseModel):
    name: str
    email: str
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''Creates a new student.'''
    db_student = Student(name=student.name, email=student.email)
    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error adding student.")
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''Creates a new course with an assigned teacher.'''
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Updated to include teacher_id
    try:
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error adding course.")
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level, "teacher_id": db_course.teacher_id}
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''Creates a new teacher.'''
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    try:
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error adding teacher.")
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''Retrieves all students.'''
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.get("/teachers/", response_model=list)
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''Retrieves all teachers.'''
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
@router.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    '''Enrolls a student in a course.'''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found.")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully."}