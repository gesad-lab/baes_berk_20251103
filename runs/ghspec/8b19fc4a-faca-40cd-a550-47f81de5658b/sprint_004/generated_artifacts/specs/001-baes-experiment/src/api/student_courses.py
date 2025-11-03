```python
# api/student_courses.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.student import Student
from models.course import Course
from db import get_db  # Assumed import for the database session
from api.errors import CourseErrors

router = APIRouter()

class CourseEnrollment(BaseModel):
    course_ids: List[int]

@router.post('/students/{student_id}/courses')
async def enroll_student_in_courses(student_id: int, enrollment: CourseEnrollment, db: Session = Depends(get_db)):
    """
    Enroll a student in specific courses.

    Args:
        student_id: ID of the student to enroll.
        enrollment: The CourseEnrollment model containing course_ids.
        db: Database session dependency.

    Returns:
        Confirmation message upon successful enrollment.

    Raises:
        HTTPException: If student or any courses do not exist.
    """
    # Validate if student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if courses exist and prepare to enroll
    courses = db.query(Course).filter(Course.id.in_(enrollment.course_ids)).all()
    if len(courses) != len(enrollment.course_ids):
        raise HTTPException(status_code=404, detail=CourseErrors.COURSE_NOT_FOUND[1])

    # Enroll student in courses - assume there's a relationship manager function
    for course in courses:
        student.courses.append(course)

    db.commit()  # Save changes to the database

    return {"message": "Enrollment successful", "enrolled_courses": [course.id for course in courses]}

@router.get('/students/{student_id}/courses')
async def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses associated with a student.

    Args:
        student_id: ID of the student.

    Returns:
        List of courses the student is enrolled in.

    Raises:
        HTTPException: If student does not exist.
    """
    # Validate if student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses associated with the student
    courses = student.courses  # Assuming a relationship is already established
    return [course.id for course in courses]
```