```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.models.enrollment import Enrollment
from src.models.student import Student
from src.models.course import Course
from src.database import get_db

app = FastAPI()

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

@app.post("/enrollments", status_code=201)
def enroll_student(enrollment: EnrollmentCreate, db: Session = next(get_db())):
    # Validate that the student exists
    student = db.query(Student).filter(Student.id == enrollment.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate that the course exists
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create the enrollment
    new_enrollment = Enrollment(student_id=enrollment.student_id, course_id=enrollment.course_id)
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    # Return the updated student information with their courses
    student_courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student.id).all()
    return {"student_id": student.id, "courses": [course.name for course in student_courses]}

@app.get("/students/{student_id}/courses", response_model=list)
def get_student_courses(student_id: int, db: Session = next(get_db())):
    # Validate that the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve the list of courses for the student
    student_courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student.id).all()
    return [{"course_id": course.id, "name": course.name} for course in student_courses]
```