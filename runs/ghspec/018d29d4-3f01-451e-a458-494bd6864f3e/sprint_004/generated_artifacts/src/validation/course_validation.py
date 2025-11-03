```python
from fastapi import HTTPException, Query
from pydantic import BaseModel
from typing import List

# Assuming we have a database model defined for Course and Student
from models import Course, Student  # Replace with actual import based on your project structure

class CourseValidationError(Exception):
    """Custom exception for course validation errors."""
    pass

def validate_course_ids(course_ids: List[int]) -> None:
    """
    Validates a list of course IDs for associations with students.
    
    Parameters:
    - course_ids: List of course IDs to validate.
    
    Raises:
    - HTTPException: If any course ID does not exist, an HTTP 400 error is raised.
    """
    # Find all valid course IDs in the database
    valid_course_ids = {course.id for course in Course.query.all()}
    
    # Check for invalid course IDs
    invalid_ids = [course_id for course_id in course_ids if course_id not in valid_course_ids]
    
    if invalid_ids:
        # Raise an HTTPException with a meaningful error message
        raise HTTPException(
            status_code=400,
            detail={"error": {
                "code": "E001",
                "message": f"Invalid course IDs: {invalid_ids}",
                "details": {
                    "valid_ids": list(valid_course_ids)
                }
            }}
        )

class CourseAssociationRequest(BaseModel):
    """Request model for associating courses with a student."""
    course_ids: List[int]

def associate_student_with_courses(student_id: int, course_ids: List[int]) -> None:
    """
    Associates a student with one or more courses after validating course IDs.
    
    Parameters:
    - student_id: ID of the student to associate courses with.
    - course_ids: List of course IDs to associate with the student.
    
    Raises:
    - CourseValidationError: If any course ID is invalid.
    """
    # Validate the course IDs
    validate_course_ids(course_ids)

    # Here, implement the logic to associate the student with the courses
    # For example, creating or updating entries in the StudentCourse join table
    # The actual database interaction logic will depend on your ORM setup
```