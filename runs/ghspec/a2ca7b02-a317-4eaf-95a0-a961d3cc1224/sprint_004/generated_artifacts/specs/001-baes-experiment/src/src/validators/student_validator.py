```python
from fastapi import HTTPException
from models.student import Student
from models.course import Course
from db.database import Database

async def validate_student_course_enrollment(student_id: int, course_id: int):
    """
    Validates the existence of a student and a course for enrollment.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.

    Raises:
        HTTPException: If either the student or course does not exist, an appropriate
        error message will be returned.
    """
    # Check if the student exists
    student = await Database.session.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail=f"E001: Invalid student ID: {student_id}")

    # Check if the course exists
    course = await Database.session.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail=f"E002: Invalid course ID: {course_id}")

    return student, course
```