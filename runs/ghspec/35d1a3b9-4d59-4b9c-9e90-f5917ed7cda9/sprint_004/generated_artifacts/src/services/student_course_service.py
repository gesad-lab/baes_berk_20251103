```python
# src/services/student_course_service.py

from typing import List
from fastapi import HTTPException
from src.repository import StudentCourses, get_student_courses, delete_student_course
from src.models import Student, Course

async def unenroll_student(student_id: int, course_id: int) -> str:
    """
    Unenroll a student from a specific course.

    Parameters:
    - student_id (int): The ID of the student to unenroll.
    - course_id (int): The ID of the course from which to unenroll the student.

    Returns:
    - str: Confirmation message indicating successful unenrollment.

    Raises:
    - HTTPException: If the student or course does not exist or if there is no enrollment to remove.
    """
    # Check if the student exists
    student = await Student.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    # Check if the course exists
    course = await Course.get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Check if the student is enrolled in the course
    enrollment = await get_student_courses(student_id, course_id)
    if not enrollment:
        raise HTTPException(status_code=400, detail="Student is not enrolled in this course.")

    # Proceed to unenroll the student from the course
    await delete_student_course(student_id, course_id)

    return "Student has been successfully unenrolled from the course."
```