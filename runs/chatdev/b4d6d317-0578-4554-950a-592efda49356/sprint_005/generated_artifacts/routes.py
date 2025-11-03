'''
Defines the API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher  # Import the Teacher model
from database import get_db
from schemas import StudentCreate, CourseCreate, TeacherCreate  # Import the TeacherCreate schema
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    Parameters:
    - student: StudentCreate - The student data to be created.
    - db: Session - The database session.
    Returns:
    - dict: The created student's details.
    '''
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
    '''
    Retrieve a list of students from the database.
    Parameters:
    - skip: int - Number of records to skip.
    - limit: int - Maximum number of records to return.
    - db: Session - The database session.
    Returns:
    - list: A list of students.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return [{"id": student.id, "name": student.name, "email": student.email} for student in students]
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course in the database.
    Parameters:
    - course: CourseCreate - The course data to be created.
    - db: Session - The database session.
    Returns:
    - dict: The created course's details.
    '''
    if not course.name:
        raise HTTPException(status_code=400, detail="Course name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="Course level is required")
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level}
@router.get("/courses/", response_model=list)
def get_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of courses from the database.
    Parameters:
    - skip: int - Number of records to skip.
    - limit: int - Maximum number of records to return.
    - db: Session - The database session.
    Returns:
    - list: A list of courses.
    '''
    courses = db.query(Course).offset(skip).limit(limit).all()
    return [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
@router.post("/students/{student_id}/courses/{course_id}", response_model=dict)
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    '''
    Enroll a student in a course.
    Parameters:
    - student_id: int - The ID of the student to enroll.
    - course_id: int - The ID of the course to enroll in.
    - db: Session - The database session.
    Returns:
    - dict: A message indicating the enrollment status.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course"}
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Create a new teacher in the database.
    Parameters:
    - teacher: TeacherCreate - The teacher data to be created.
    - db: Session - The database session.
    Returns:
    - dict: The created teacher's details.
    '''
    if not teacher.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not teacher.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}