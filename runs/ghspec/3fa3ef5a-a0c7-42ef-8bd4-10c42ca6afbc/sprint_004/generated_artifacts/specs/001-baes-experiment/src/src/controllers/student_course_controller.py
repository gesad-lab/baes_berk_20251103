```python
# src/controllers/student_course_controller.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.services.student_course_service import StudentCourseService
from src.models.student import Student
from src.models.course import Course
from src.database import get_db

router = APIRouter()

@router.post("/students/{student_id}/courses")
async def assign_courses_to_student(student_id: int, course_ids: list[int], db: Session = Depends(get_db)):
    """
    Assign one or more courses to a specific student.

    Args:
        student_id (int): The ID of the student to whom courses will be assigned.
        course_ids (list[int]): A list of course IDs to be assigned.

    Returns:
        Student: The updated student object including the newly assigned courses.

    Raises:
        HTTPException: If the student or any of the courses do not exist.
    """
    try:
        student = StudentCourseService.assign_courses(student_id, course_ids, db)
        return student
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/students/{student_id}")
async def retrieve_student_with_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve student details, including their associated courses.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        Student: The student object with associated courses.

    Raises:
        HTTPException: If the student does not exist.
    """
    student = StudentCourseService.get_student_with_courses(student_id, db)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/students/{student_id}/courses/{course_id}")
async def remove_course_from_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Remove a specific course from a student's list of courses.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course to remove.

    Returns:
        Student: The updated student object after course removal.

    Raises:
        HTTPException: If the student or course does not exist or if the course is not assigned.
    """
    try:
        student = StudentCourseService.remove_course(student_id, course_id, db)
        return student
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
```