'''
API routes for the application.
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Teacher
from database import get_db
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
router = APIRouter()
@router.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student.
    '''
    try:
        db_student = Student(name=student.name, email=student.email)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/students/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    '''
    Retrieve all students along with their enrolled courses.
    '''
    students = db.query(Student).all()
    return [
        StudentResponse(
            id=student.id,
            name=student.name,
            email=student.email,
            courses=[course.id for course in student.courses]
        ) for student in students
    ]
@router.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    '''
    Create a new course with an associated teacher.
    '''
    try:
        # Validate teacher_id
        if course.teacher_id:
            teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
            if not teacher:
                raise HTTPException(status_code=404, detail="Teacher not found")
        db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return CourseResponse(id=db_course.id, name=db_course.name, level=db_course.level, teacher_id=db_course.teacher_id)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
@router.post("/students/{student_id}/courses/{course_id}")
def enroll_student_in_course(student_id: int, course_id: int, db: Session = Depends(get_db)):
    '''
    Enroll a student in a course.
    '''
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    if course in student.courses:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled in course successfully"}
@router.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    '''
    Create a new teacher.
    '''
    try:
        db_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return TeacherResponse(id=db_teacher.id, name=db_teacher.name, email=db_teacher.email)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
@router.get("/teachers/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    '''
    Retrieve all teachers.
    '''
    teachers = db.query(Teacher).all()
    return [TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email) for teacher in teachers]