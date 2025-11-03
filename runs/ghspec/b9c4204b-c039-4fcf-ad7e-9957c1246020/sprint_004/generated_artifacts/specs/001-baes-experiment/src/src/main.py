from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from src.database import get_db
from src.models import Student, Course, StudentCourse  # Assuming models are defined in src/models

app = FastAPI()

class Enrollment(BaseModel):
    student_id: int
    course_id: int

@app.post("/enroll")
async def enroll_student(enrollment: Enrollment, db: Session = Depends(get_db)):
    """
    Enroll a student in a course.

    Args:
        enrollment (Enrollment): The enrollment data containing student_id and course_id.
        db (Session): The SQLAlchemy database session.

    Returns:
        JSON response confirming enrollment status.
    """
    # Check if the student and course exist
    student = db.query(Student).filter(Student.id == enrollment.student_id).first()
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Check if the student is already enrolled
    existing_enrollment = db.query(StudentCourse).filter(
        StudentCourse.student_id == enrollment.student_id,
        StudentCourse.course_id == enrollment.course_id
    ).first()

    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")

    # Enroll the student in the course
    new_enrollment = StudentCourse(student_id=enrollment.student_id, course_id=enrollment.course_id)
    db.add(new_enrollment)
    db.commit()

    return {"status": "success", "message": "Student enrolled successfully"}

@app.get("/students/{student_id}/courses", response_model=List[Course])
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses for a specific student.

    Args:
        student_id (int): The ID of the student to retrieve courses for.
        db (Session): The SQLAlchemy database session.

    Returns:
        List of Course entities associated with the student.
    """
    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()

    return courses