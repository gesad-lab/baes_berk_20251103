'''
Defines the API endpoints for the Student, Course, and Teacher entities.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher  # Added Teacher import
from database import get_db
from schemas import StudentCreate, CourseCreate, TeacherCreate  # Added TeacherCreate import
router = APIRouter()
@router.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
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
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
@router.post("/courses/", response_model=dict)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    if not course.name:
        raise HTTPException(status_code=400, detail="Course name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="Course level is required")
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Update this line
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return {"id": db_course.id, "name": db_course.name, "level": db_course.level, "teacher_id": db_course.teacher_id}
@router.get("/courses/", response_model=list)
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()
@router.post("/students/{student_id}/courses/{course_id}/enroll")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    if course in student.courses:  # Check for duplicate enrollment
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully"}
@router.post("/teachers/", response_model=dict)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    if not teacher.name:
        raise HTTPException(status_code=400, detail="Name is required")
    if not teacher.email:
        raise HTTPException(status_code=400, detail="Email is required")
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"id": db_teacher.id, "name": db_teacher.name, "email": db_teacher.email}
@router.get("/teachers/", response_model=list)
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()