```python
# src/services/course_service.py

from typing import Optional
from src.models import Course, Teacher  # Assuming your models are in src/models
from src.database import get_course_by_id, get_teacher_by_id, update_course  # Adjust based on your DAL
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

class CourseService:
    """Service layer for managing course-related operations."""

    @staticmethod
    def assign_teacher_to_course(course_id: int, teacher_id: int) -> Course:
        """
        Assign a teacher to a course.

        Args:
            course_id (int): The ID of the course.
            teacher_id (int): The ID of the teacher to assign.

        Returns:
            Course: The updated course with the assigned teacher information.
        
        Raises:
            HTTPException: If the course or teacher is invalid or if assignment fails.
        """
        course = get_course_by_id(course_id)
        if not course:
            logger.error(f"Course with ID {course_id} not found.")
            raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")

        teacher = get_teacher_by_id(teacher_id)
        if not teacher:
            logger.error(f"Teacher with ID {teacher_id} not found.")
            raise HTTPException(status_code=404, detail=f"Teacher with ID {teacher_id} not found.")

        # Assign teacher to the course
        course.teacher_id = teacher_id
        updated_course = update_course(course)

        logger.info(f"Assigned Teacher ID {teacher_id} to Course ID {course_id}.")
        return updated_course

    @staticmethod
    def retrieve_course_with_teacher(course_id: int) -> Course:
        """
        Retrieve course details including associated teacher information.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The course details, including teacher information.

        Raises:
            HTTPException: If the course is not found.
        """
        course = get_course_by_id(course_id)
        if not course:
            logger.error(f"Course with ID {course_id} not found.")
            raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")

        return course

    @staticmethod
    def update_teacher_for_course(course_id: int, new_teacher_id: int) -> Course:
        """
        Update the teacher assigned to a course.

        Args:
            course_id (int): The ID of the course to update.
            new_teacher_id (int): The ID of the new teacher to assign.

        Returns:
            Course: The updated course with the new teacher information.

        Raises:
            HTTPException: If the course or new teacher is invalid.
        """
        course = get_course_by_id(course_id)
        if not course:
            logger.error(f"Course with ID {course_id} not found for update.")
            raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")

        new_teacher = get_teacher_by_id(new_teacher_id)
        if not new_teacher:
            logger.error(f"New Teacher with ID {new_teacher_id} not found for course update.")
            raise HTTPException(status_code=404, detail=f"Teacher with ID {new_teacher_id} not found.")

        # Update the teacher for the course
        course.teacher_id = new_teacher_id
        updated_course = update_course(course)

        logger.info(f"Updated Course ID {course_id} with new Teacher ID {new_teacher_id}.")
        return updated_course
```