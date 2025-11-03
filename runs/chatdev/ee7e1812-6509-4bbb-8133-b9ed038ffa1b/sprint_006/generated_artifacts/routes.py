'''
Contains the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import get_db
from schemas import StudentCreate, CourseCreate, TeacherCreate  # Import the Pydantic models
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Creates a new student in the database and enrolls them in courses.
    '''
    try:
        db_student = Student(name=student.name, email=student.email)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        # Enroll in courses
        if student.course_ids:
            courses = db.query(Course).filter(Course.id.in_(student.course_ids)).all()
            db_student.courses.extend(courses)
            db.commit()
        return {"id": db_student.id, "name": db_student.name, "email": db_student.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieves a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Creates a new course in the database.
    '''
    try:
        db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Added teacher_id
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieves a list of courses from the database.
    '''
    courses = db.query(Course).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level, "teacher_id": course.teacher_id} for course in courses]
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Creates a new teacher in the database.
    '''
    try:
        db_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/teachers/", response_model=list)
def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieves a list of teachers from the database.
    '''
    teachers = db.query(Teacher).offset(skip).limit(limit).all()
    return [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]