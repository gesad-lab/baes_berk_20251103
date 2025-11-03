'''
Contains the CRUD operations for the Student and Course entities.
'''
from sqlalchemy.orm import Session
from models import Student, Course
from schemas import StudentCreate, CourseCreate
def create_student(db: Session, student: StudentCreate):
    '''
    Creates a new student in the database.
    '''
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
def get_students(db: Session, skip: int = 0, limit: int = 10):
    '''
    Retrieves a list of students from the database with pagination.
    '''
    return db.query(Student).offset(skip).limit(limit).all()
def create_course(db: Session, course: CourseCreate):
    '''
    Creates a new course in the database.
    '''
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
def get_courses(db: Session, skip: int = 0, limit: int = 10):
    '''
    Retrieves a list of courses from the database with pagination.
    '''
    return db.query(Course).offset(skip).limit(limit).all()
def add_course_to_student(db: Session, student_id: int, course_id: int):
    '''
    Adds a course to a student's list of courses.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if student and course:
        student.courses.append(course)
        db.commit()
        db.refresh(student)
    return student