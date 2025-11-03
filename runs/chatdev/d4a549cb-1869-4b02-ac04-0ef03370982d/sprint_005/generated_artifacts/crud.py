'''
Contains functions for creating and retrieving Student, Course, and Teacher records.
'''
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from schemas import StudentCreate, CourseCreate, TeacherCreate
async def create_student(student: StudentCreate, db: Session):
    db_student = Student(name=student.name, email=student.email)
    # Handle course enrollment
    if student.course_ids:
        db_student.courses = db.query(Course).filter(Course.id.in_(student.course_ids)).all()
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
async def get_students(db: Session):
    return db.query(Student).all()
async def create_course(course: CourseCreate, db: Session):
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
async def get_courses(db: Session):
    return db.query(Course).all()
async def create_teacher(teacher: TeacherCreate, db: Session):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
async def get_teachers(db: Session):
    return db.query(Teacher).all()