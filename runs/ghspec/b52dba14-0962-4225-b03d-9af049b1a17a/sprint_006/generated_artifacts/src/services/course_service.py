```python
import logging
from typing import Optional, Dict, Any
from src.models.course_model import Course
from src.models.teacher_model import Teacher
from src.database import db  # Assuming a SQLAlchemy-like database setup

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CourseService:
    """Service for managing courses in the system."""

    @staticmethod
    def assign_teacher_to_course(course_id: int, teacher_id: int) -> Dict[str, Any]:
        """Assign a teacher to a course.

        Args:
            course_id (int): The ID of the course to assign the teacher to.
            teacher_id (int): The ID of the teacher to be assigned.

        Returns:
            dict: Result of the operation with success status and message.
        """
        try:
            # Fetch the course and teacher from the database
            course = db.session.query(Course).filter(Course.id == course_id).first()
            teacher = db.session.query(Teacher).filter(Teacher.id == teacher_id).first()

            # Check if the course and teacher exist
            if not course:
                logger.error(f"Course with ID {course_id} does not exist.")
                return {"success": False, "message": "Course does not exist."}
            if not teacher:
                logger.error(f"Teacher with ID {teacher_id} does not exist.")
                return {"success": False, "message": "Teacher does not exist."}

            # Assign the teacher to the course
            course.teacher_id = teacher.id
            db.session.commit()
            logger.info(f"Teacher with ID {teacher_id} assigned to course with ID {course_id}.")
            return {"success": True, "message": "Teacher assigned to course successfully."}

        except Exception as e:
            logger.exception("An error occurred while assigning teacher to course.")
            db.session.rollback()
            return {"success": False, "message": "An unexpected error occurred."}

    @staticmethod
    def get_course_details(course_id: int) -> Dict[str, Any]:
        """Retrieve course details including assigned teacher.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            dict: Course details including teacher information, if assigned.
        """
        try:
            course = db.session.query(Course).filter(Course.id == course_id).first()
            if not course:
                logger.error(f"Course with ID {course_id} does not exist.")
                return {"success": False, "message": "Course does not exist."}

            # Prepare course details with teacher information
            course_details = {
                "course_id": course.id,
                "course_name": course.name,
                "teacher_id": course.teacher_id,
                "teacher_name": course.teacher.name if course.teacher else None
            }
            logger.info(f"Retrieved details for course ID {course_id}.")
            return {"success": True, "data": course_details}

        except Exception as e:
            logger.exception("An error occurred while retrieving course details.")
            return {"success": False, "message": "An unexpected error occurred."}
```