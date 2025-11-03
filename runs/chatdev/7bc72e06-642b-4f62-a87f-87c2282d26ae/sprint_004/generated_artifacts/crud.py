'''
CRUD operations for the Student and Course entities.
'''
from sqlalchemy.orm import Session
from models import Student, Course
from schemas import StudentCreate, CourseCreate
def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, email=student.email)  # Updated to handle email
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
def add_course_to_student(db: Session, student_id: int, course_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if student and course:
        student.courses.append(course)
        db.commit()
        db.refresh(student)
    return student
def get_student_courses(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    return student.courses if student else None