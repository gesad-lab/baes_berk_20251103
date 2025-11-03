```python
# src/error_handlers/error_responses.py

from fastapi import HTTPException, status
from typing import Dict

class ErrorResponseHandler:
    """Centralized error handling for API responses."""

    @staticmethod
    def handle_course_not_found(course_id: int) -> HTTPException:
        """Handle the case where a course is not found.
        
        Args:
            course_id (int): The ID of the course that was not found.

        Returns:
            HTTPException: An HTTP exception with a 404 status and error message.
        """
        error_message = {
            "error": {
                "code": "E404",
                "message": f"Course with ID {course_id} not found.",
                "details": {}
            }
        }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_message)

    @staticmethod
    def handle_student_not_found(student_id: int) -> HTTPException:
        """Handle the case where a student is not found.
        
        Args:
            student_id (int): The ID of the student that was not found.

        Returns:
            HTTPException: An HTTP exception with a 404 status and error message.
        """
        error_message = {
            "error": {
                "code": "E404",
                "message": f"Student with ID {student_id} not found.",
                "details": {}
            }
        }
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_message)

    @staticmethod
    def handle_invalid_course_assignment(course_id: int, student_id: int) -> HTTPException:
        """Handle errors that occur during course assignment to a student.
        
        Args:
            course_id (int): The ID of the invalid course being assigned.
            student_id (int): The ID of the student receiving the course.

        Returns:
            HTTPException: An HTTP exception indicating the assignment failure.
        """
        error_message = {
            "error": {
                "code": "E400",
                "message": f"Cannot assign course ID {course_id} to student ID {student_id}. Course does not exist.",
                "details": {}
            }
        }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
```