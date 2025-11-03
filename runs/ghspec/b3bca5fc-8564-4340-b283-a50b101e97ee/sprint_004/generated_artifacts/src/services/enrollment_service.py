```python
from typing import Dict, Any
from flask import jsonify, request
from your_project.models import Course, Student  # Adjust the import as per your project structure
from your_project.db import session  # Assuming you have a session for database access
from your_project.exceptions import InvalidInputError  # Custom exception for invalid input errors

class EnrollmentService:
    """Service for handling student enrollments in courses."""

    @staticmethod
    def enroll_student(student_id: str, course_id: str) -> Dict[str, Any]:
        """Enroll a student in a specified course.
        
        Args:
            student_id (str): The ID of the student.
            course_id (str): The ID of the course to enroll in.

        Returns:
            Dict[str, Any]: A confirmation message including student ID and course ID.

        Raises:
            InvalidInputError: If the course_id is invalid or does not exist.
        """
        # Validate input
        EnrollmentService.validate_enrollment_input(course_id)

        # Logic to enroll the student in the course
        # Assuming you have a method that adds an entry to the student_courses table
        EnrollmentService.add_student_to_course(student_id, course_id)

        return {
            "message": "Student enrolled successfully.",
            "student_id": student_id,
            "course_id": course_id
        }

    @staticmethod
    def validate_enrollment_input(course_id: str) -> None:
        """Validate the course_id for enrollment.
        
        Args:
            course_id (str): The ID of the course to validate.

        Raises:
            InvalidInputError: If the course_id does not exist.
        """
        # Check if the course_id exists in the database
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            raise InvalidInputError(f"E001: Course with id '{course_id}' does not exist.")

    @staticmethod
    def add_student_to_course(student_id: str, course_id: str) -> None:
        """Add a student to the specified course in the junction table.

        Args:
            student_id (str): The ID of the student.
            course_id (str): The ID of the course.
        """
        # Logic to add the student to the junction table (student_courses)
        # Ensure to handle any exceptions that may arise during the process
        try:
            # Assuming you have a junction table model called StudentCourse
            student_course_entry = StudentCourse(student_id=student_id, course_id=course_id)
            session.add(student_course_entry)
            session.commit()
        except Exception as e:
            session.rollback()
            raise ValueError("Failed to enroll student in the course.") from e
```
