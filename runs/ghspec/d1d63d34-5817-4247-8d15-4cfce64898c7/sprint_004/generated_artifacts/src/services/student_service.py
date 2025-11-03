```python
from typing import List
from fastapi import HTTPException
from src.models import Student  # Assuming Student model is in src/models

def remove_course_from_student(student_id: int, course_id: int) -> None:
    """Remove a course from a student's list of courses.

    Args:
        student_id (int): The ID of the student from whom to remove the course.
        course_id (int): The ID of the course to be removed.

    Raises:
        HTTPException: If the student is not found or the course is not assigned to the student.
    """
    student = get_student_by_id(student_id)  # Assuming a function to get student by ID

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if course_id not in student.courses:
        raise HTTPException(status_code=400, detail="Course not assigned to student")

    # Remove the course from the student's list of courses
    student.courses.remove(course_id)

    # Assuming a function to update the student object in the database
    update_student(student)  # Function to persist changes
```