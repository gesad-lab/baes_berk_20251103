```python
from typing import List
from fastapi import HTTPException
from src.models.course import Course
from src.repositories.student_course_repository import get_valid_course_ids

class StudentCourseService:
    def __init__(self, student_repository, course_repository):
        self.student_repository = student_repository
        self.course_repository = course_repository

    def enroll_student_in_courses(self, student_id: int, course_ids: List[int]) -> None:
        """
        Enroll a student in the specified courses after validating the course IDs.

        Parameters:
        - student_id (int): The ID of the student to enroll.
        - course_ids (List[int]): A list of course IDs to enroll the student in.

        Raises:
        - HTTPException: If any of the course IDs are invalid.
        """
        # Validate course IDs by checking against existing course IDs
        valid_course_ids = get_valid_course_ids()  # This should return a list of all valid course IDs
        invalid_ids = [cid for cid in course_ids if cid not in valid_course_ids]

        if invalid_ids:
            # Raise an error if any invalid course IDs are detected
            raise HTTPException(
                status_code=400,
                detail={
                    "error": {
                        "code": "E002",
                        "message": "Invalid Course IDs provided.",
                        "details": {
                            "invalid_ids": invalid_ids
                        }
                    }
                }
            )

        # Proceed with enrollment in valid courses
        self.student_repository.enroll_student(student_id, course_ids)

    def retrieve_student_courses(self, student_id: int):
        """
        Retrieve the student information along with their associated course IDs.

        Parameters:
        - student_id (int): The ID of the student to retrieve information for.

        Returns:
        - dict: Student details including course IDs.
        """
        student = self.student_repository.get_student(student_id)
        enrolled_courses = self.course_repository.get_courses_by_student_id(student_id)

        return {
            "student": student,
            "enrolled_courses": enrolled_courses
        }
```