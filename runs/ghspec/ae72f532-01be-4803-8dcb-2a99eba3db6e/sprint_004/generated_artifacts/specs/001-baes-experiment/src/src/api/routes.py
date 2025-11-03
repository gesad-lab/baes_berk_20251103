```python
from fastapi import APIRouter, HTTPException, Body
from typing import List
from src.models.student import Student  # Assuming Student model has been updated with courses
from src.services.student_service import StudentService

router = APIRouter()

@router.post("/students/{student_id}/enroll", response_model=Student)
async def enroll_student_in_courses(student_id: int, course_ids: List[int] = Body(...)):
    """
    Enroll a student in one or more courses.

    :param student_id: ID of the student to enroll.
    :param course_ids: List of course IDs to enroll the student into.
    :return: Updated Student object with associated course IDs.
    :raises HTTPException: If the student is not found or if any course IDs are invalid.
    """
    
    # Validate student existence
    student = StudentService.get_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")
    
    # Validate course IDs
    invalid_course_ids = StudentService.validate_course_ids(course_ids)
    if invalid_course_ids:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E004",
                    "message": "Invalid course IDs provided.",
                    "details": {"invalid_ids": invalid_course_ids}
                }
            }
        )
    
    # Enroll the student in courses and return updated student
    updated_student = StudentService.enroll_in_courses(student, course_ids)
    return updated_student


@router.get("/students/{student_id}/courses", response_model=Student)
async def get_student_courses(student_id: int):
    """
    Retrieve a student's enrolled courses.

    :param student_id: ID of the student to retrieve courses for.
    :return: Student object with associated course IDs.
    :raises HTTPException: If the student is not found.
    """
    
    # Validate student existence
    student = StudentService.get_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")
    
    return student
```