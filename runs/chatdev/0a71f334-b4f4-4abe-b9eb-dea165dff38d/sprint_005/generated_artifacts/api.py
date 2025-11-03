'''
API endpoints for managing students, courses, and teachers.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, course_ids: list[int] = [], db: Session = Depends(get_db)):
    try:
        db_student = Student(name=student.name, email=student.email)
        if course_ids:
            db_student.courses = db.query(Course).filter(Course.id.in_(course_ids)).all()
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/students/", response_model=list[StudentResponse])
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        students = db.query(Student).options(joinedload(Student.courses)).offset(skip).limit(limit).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    try:
        db_course = Course(name=course.name, level=course.level)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return db_course
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/courses/", response_model=list[CourseResponse])
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        courses = db.query(Course).offset(skip).limit(limit).all()
        return courses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    try:
        db_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        teachers = db.query(Teacher).offset(skip).limit(limit).all()
        return teachers
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))