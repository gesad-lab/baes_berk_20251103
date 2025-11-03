'''
API routes for student, course, and teacher-related operations.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import get_db
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
router = APIRouter()
@router.post("/students/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    """
    Create a new student in the database.
    """
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    """
    Retrieve all students from the database.
    """
    students = db.query(Student).all()
    return students
@router.post("/courses/", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course in the database.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@router.get("/courses/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve all courses from the database.
    """
    courses = db.query(Course).all()
    return courses
@router.post("/teachers/", response_model=TeacherResponse, status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher in the database.
    """
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@router.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    """
    Retrieve all teachers from the database.
    """
    teachers = db.query(Teacher).all()
    return teachers
@router.post("/students/{student_id}/courses/{course_id}", status_code=204)
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Enroll a student in a course.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
@router.post("/courses/{course_id}/assign_teacher/{teacher_id}", status_code=204)
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Assign a teacher to a course.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not course or not teacher:
        raise HTTPException(status_code=404, detail="Course or Teacher not found")
    course.teacher = teacher
    db.commit()