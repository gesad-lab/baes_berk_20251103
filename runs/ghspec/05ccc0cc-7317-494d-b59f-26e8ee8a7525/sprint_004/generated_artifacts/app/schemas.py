```python
# app/routes/enrollment.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Student, Course, Enrollment
from app.schemas import StudentResponse, EnrollmentRequest
from app.database import get_db

router = APIRouter()

@router.post("/students/{student_id}/enroll", response_model=StudentResponse)
async def enroll_student(student_id: int, enrollment: EnrollmentRequest, db: Session = Depends(get_db)):
    """Enroll a student in a course."""

    # Retrieve the student by ID
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=400, detail="Invalid course ID.")

    # Create an enrollment entry
    new_enrollment = Enrollment(student_id=student_id, course_id=enrollment.course_id)
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    # Return the updated student details including enrolled courses
    student_with_courses = db.query(Student).filter(Student.id == student_id).first()
    return student_with_courses

@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student_details(student_id: int, db: Session = Depends(get_db)):
    """Retrieve student details including their enrolled courses."""

    # Retrieve the student details
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    # Prepare the response with enrolled courses
    enrolled_courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()
    student_data = {
        "id": student.id,
        "name": student.name,
        "enrolled_courses": enrolled_courses
    }
    return student_data
```