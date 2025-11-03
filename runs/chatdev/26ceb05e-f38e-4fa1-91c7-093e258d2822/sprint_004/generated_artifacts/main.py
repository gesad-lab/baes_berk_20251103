'''
Entry point of the application that initializes the FastAPI app and sets up the routes.
'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import create_student, get_students, create_course, get_courses, enroll_student_in_course
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)
@app.get("/students/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db=db)
@app.post("/courses/", response_model=CourseResponse)
def add_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)
@app.get("/courses/", response_model=list[CourseResponse])
def read_courses(db: Session = Depends(get_db)):
    return get_courses(db=db)
@app.post("/enroll/", response_model=dict)
def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    enroll_student_in_course(db=db, student_id=student_id, course_id=course_id)
    return {"message": "Student enrolled in course successfully"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)