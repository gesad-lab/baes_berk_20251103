'''
Contains functions for database operations related to the Student, Teacher, and Course entities.
'''
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment, Teacher
from schemas import StudentCreate, CourseCreate, TeacherCreate
def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, email=student.email)  # Include email in the creation
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
def get_students(db: Session):
    return db.query(Student).all()
def create_course(db: Session, course: CourseCreate):
    # Validate that the teacher_id exists
    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    if not teacher:
        raise ValueError("Teacher ID does not exist.")
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Update this line
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
def get_courses(db: Session):
    return db.query(Course).all()
def enroll_student_in_course(db: Session, student_id: int, course_id: int):
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment
def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
def get_teachers(db: Session):
    return db.query(Teacher).all()