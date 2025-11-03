```python
# src/api.py

from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from models import Student, Course, StudentCourses
from sqlalchemy.orm import Session
from database import get_db  # assuming you have a get_db function to get the session

app = FastAPI()

# Pydantic model for course enrollment
class EnrollmentRequest(BaseModel):
    course_id: int

@app.post("/students/{student_id}/enroll", status_code=201)
def enroll_student(student_id: int, enrollment: EnrollmentRequest, db: Session = Depends(get_db)):
    # Check if the course exists
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=400, detail=f"E001: Course ID {enrollment.course_id} does not exist.")

    # Link student to course
    student_course = StudentCourses(student_id=student_id, course_id=enrollment.course_id)
    
    db.add(student_course)
    db.commit()
    db.refresh(student_course)

    return {"message": "Student successfully enrolled in the course."}

@app.get("/students/{student_id}/courses", status_code=200)
def get_courses_for_student(student_id: int, db: Session = Depends(get_db)):
    # Retrieve courses for the student
    courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
    
    if not courses:
        raise HTTPException(status_code=404, detail="No courses found for this student.")
    
    return courses
```