'''
Main application file for the FastAPI backend.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import init_db, get_db
from models import Student, Course, Teacher
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse, TeacherCreate, TeacherResponse
app = FastAPI()
# Initialize the database
init_db()
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)  # Added email field
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, level=course.level, teacher_id=course.teacher_id)  # Updated to include teacher_id
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
@app.get("/courses/{course_id}", response_model=CourseResponse)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course
@app.post("/students/{student_id}/enroll/{course_id}")
def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_student is None or db_course is None:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    db_student.courses.append(db_course)
    db.commit()
    return {"msg": "Student enrolled in course successfully"}
@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher