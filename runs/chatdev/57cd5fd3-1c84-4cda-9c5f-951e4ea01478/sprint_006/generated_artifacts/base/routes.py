'''
API routes for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import get_db
from schemas import StudentCreate, CourseCreate, TeacherCreate
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if not student.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not student.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    if not course.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="Level is required")
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    if not teacher.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not teacher.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.post("/students/{student_id}/courses/{course_id}/", response_model=dict)
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_student or not db_course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    db_student.courses.append(db_course)
    db.commit()
    return {"student_id": db_student.id, "course_id": db_course.id}