```python
# src/services/course_service.py

from models.course import Course  # Import the Course model
from models.teacher import Teacher  # Import the Teacher model
from sqlalchemy.orm import Session
from typing import Optional

class CourseService:
    """Service class for managing course-related business logic."""

    @staticmethod
    def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session) -> Optional[Course]:
        """Assign a teacher to a course.

        Args:
            course_id (int): The ID of the course to which the teacher will be assigned.
            teacher_id (int): The ID of the teacher to assign to the course.
            db (Session): SQLAlchemy session for database interactions.

        Returns:
            Course: The updated course with the assigned teacher.
        """
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise ValueError(f"Course with ID {course_id} not found.")
        
        # Assign the teacher by updating the teacher_id
        course.teacher_id = teacher_id
        db.commit()  # Commit the changes to the database
        return course

    @staticmethod
    def remove_teacher_from_course(course_id: int, db: Session) -> Optional[Course]:
        """Remove the teacher assignment from a course.

        Args:
            course_id (int): The ID of the course from which the teacher will be removed.
            db (Session): SQLAlchemy session for database interactions.

        Returns:
            Course: The updated course without the teacher.
        """
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise ValueError(f"Course with ID {course_id} not found.")

        # Remove the teacher assignment by setting teacher_id to None
        course.teacher_id = None
        db.commit()  # Commit the changes to the database
        return course

    @staticmethod
    def get_course_details(course_id: int, db: Session) -> Optional[dict]:
        """Retrieve details of a specific course including teacher information.

        Args:
            course_id (int): The ID of the course to retrieve details for.
            db (Session): SQLAlchemy session for database interactions.

        Returns:
            dict: Course details including teacher's name and email.
        """
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise ValueError(f"Course with ID {course_id} not found.")
        
        # Prepare the course details to include the teacher's name and email if assigned
        course_details = {
            "course_id": course.id,
            "course_name": course.name,
            "teacher": {
                "name": course.teacher.name if course.teacher else None,
                "email": course.teacher.email if course.teacher else None
            }
        }
        return course_details
```