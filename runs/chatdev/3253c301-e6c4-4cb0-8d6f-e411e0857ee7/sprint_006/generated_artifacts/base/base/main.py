'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_student, get_students, create_course, get_courses
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse
app = FastAPI()
@app.post("/students/", response_model=StudentResponse)
def create_student_endpoint(student: StudentCreate, course_ids: list[int] = None, db: Session = Depends(get_db)):
    try:
        return create_student(db=db, student=student, course_ids=course_ids)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/students/", response_model=list[StudentResponse])
def get_students_endpoint(db: Session = Depends(get_db)):
    students = get_students(db=db)
    if not students:
        raise HTTPException(status_code=404, detail="No students found")
    return students
@app.post("/courses/", response_model=CourseResponse)
def create_course_endpoint(course: CourseCreate, db: Session = Depends(get_db)):
    try:
        return create_course(db=db, course=course)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/courses/", response_model=list[CourseResponse])
def get_courses_endpoint(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    if not courses:
        raise HTTPException(status_code=404, detail="No courses found")
    return courses
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)