```python
import logging
from typing import Any, Dict

from src.models.enrollment_model import Enrollment
from src.models.student_model import Student
from src.models.course_model import Course
from src.database import db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnrollmentService:
    """Service for managing student course enrollments."""

    @staticmethod
    def enroll_student_in_course(student_id: int, course_id: int) -> Dict[str, Any]:
        """Enroll a student in a course.

        Args:
            student_id (int): The ID of the student.
            course_id (int): The ID of the course.

        Returns:
            Dict[str, Any]: The result of the enrollment operation.
        """
        # Validate student ID
        student = Student.query.get(student_id)
        if not student:
            logger.error("Invalid student ID: %s", student_id)
            return {"error": {"code": "E001", "message": "Invalid student ID."}}

        # Validate course ID
        course = Course.query.get(course_id)
        if not course:
            logger.error("Invalid course ID: %s", course_id)
            return {"error": {"code": "E002", "message": "Invalid course ID."}}

        # Create enrollment
        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        db.session.add(enrollment)
        db.session.commit()

        logger.info("Student %s enrolled in course %s.", student_id, course_id)
        return {"message": "Enrollment successful."}

    @staticmethod
    def remove_course_from_student(student_id: int, course_id: int) -> Dict[str, Any]:
        """Remove a course from a student's profile.

        Args:
            student_id (int): The ID of the student.
            course_id (int): The ID of the course.

        Returns:
            Dict[str, Any]: The result of the removal operation.
        """
        # Fetch the enrollment record to remove
        enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
        if not enrollment:
            logger.warning("Enrollment not found for student %s and course %s.", student_id, course_id)
            return {"error": {"code": "E003", "message": "Enrollment not found."}}

        db.session.delete(enrollment)
        db.session.commit()

        logger.info("Course %s removed from student %s.", course_id, student_id)
        return {"message": "Course successfully removed from student."}
```