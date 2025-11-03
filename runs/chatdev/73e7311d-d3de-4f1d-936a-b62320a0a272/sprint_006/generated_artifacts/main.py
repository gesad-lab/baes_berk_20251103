'''
Main application entry point.
'''
import uvicorn
from fastapi import FastAPI, HTTPException
from database import init_db, get_db
from models import Course, Student, Teacher
from schemas import CourseCreate, CourseResponse, StudentCreate, StudentResponse, TeacherCreate, TeacherResponse
app = FastAPI()
# Initialize the database
init_db()
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate):
    db = next(get_db())
    # Check if the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=400, detail="Teacher not found")
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/{course_id}", response_model=CourseResponse)
def read_course(course_id: int):
    db = next(get_db())
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate):
    db = next(get_db())
    db_student = Student(name=student.name, email=student.email)
    db_student.courses = db.query(Course).filter(Course.id.in_(student.course_ids)).all()
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int):
    db = next(get_db())
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate):
    db = next(get_db())
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def read_teacher(teacher_id: int):
    db = next(get_db())
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher