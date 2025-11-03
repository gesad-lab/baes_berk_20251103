'''
Contains functions for creating and retrieving Student and Course records.
'''
from sqlalchemy.orm import Session
from models import Student, Course
from schemas import StudentCreate, CourseCreate
def create_student(db: Session, student: StudentCreate, course_ids: list[int] = None):
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    if course_ids:
        db_student.courses = db.query(Course).filter(Course.id.in_(course_ids)).all()
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
def get_students(db: Session):
    return db.query(Student).all()
def create_course(db: Session, course: CourseCreate):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
def get_courses(db: Session):
    return db.query(Course).all()