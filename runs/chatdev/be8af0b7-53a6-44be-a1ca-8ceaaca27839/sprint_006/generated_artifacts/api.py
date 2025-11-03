'''
Contains API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student as StudentModel, Course as CourseModel, Teacher as TeacherModel
from schemas import StudentCreate, CourseCreate, TeacherCreate  # Import the Pydantic models
from database import get_db
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Creates a new student.
    '''
    if not student.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not student.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_student = StudentModel(name=student.name, email=student.email)  # Include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    # Associate courses if provided
    if student.courses:
        db_student.courses = db.query(CourseModel).filter(CourseModel.id.in_(student.courses)).all()
        db.commit()
    return {"id": db_student.id, "name": db_student.name, "email": db_student.email}  # Include email in response
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Creates a new course and associates it with a teacher if provided.
    '''
    if not course.name:
        raise HTTPException(status_code=400, detail="Course name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="Course level is required")
    db_course = CourseModel(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Update this line
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level, "teacher_id": db_course.teacher_id}  # Include teacher_id in response
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Creates a new teacher.
    '''
    if not teacher.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not teacher.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_teacher = TeacherModel(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/students/", response_model=list)
def get_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieves all students.
    '''
    students = db.query(StudentModel).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email, "courses": [course.id for course in student.courses]} for student in students]  # Include email and courses in response
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieves all courses.
    '''
    courses = db.query(CourseModel).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level, "teacher_id": course.teacher_id} for course in courses]  # Include teacher_id in response