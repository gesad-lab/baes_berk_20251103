```python
# src/services.py

from typing import Optional
from src.models import Course, Teacher, db  # Import Course and Teacher models for interaction with the database

class CourseService:
    """Service class for managing courses and their relationships with teachers."""

    @staticmethod
    def create_course(course_data: dict) -> Course:
        """Create a new course and optionally assign a teacher.

        Args:
            course_data (dict): A dictionary containing course information, including optional 'teacher_id'.

        Returns:
            Course: The created course object.

        Raises:
            ValueError: If required fields are missing in course_data.
        """
        if 'name' not in course_data:
            raise ValueError("Course data must contain 'name' field.")

        course = Course(name=course_data['name'], teacher_id=course_data.get('teacher_id'))
        
        # Add course to the session and commit
        db.session.add(course)
        db.session.commit()
        
        return course

    @staticmethod
    def update_course(course_id: int, update_data: dict) -> Optional[Course]:
        """Update an existing course with new data.

        Args:
            course_id (int): The ID of the course to update.
            update_data (dict): A dictionary containing updated course information.

        Returns:
            Optional[Course]: The updated course object or None if not found.
        """
        course = Course.query.get(course_id)
        if course is None:
            return None  # If the course does not exist, return None

        # Update course attributes
        if 'name' in update_data:
            course.name = update_data['name']
        if 'teacher_id' in update_data:
            course.teacher_id = update_data.get('teacher_id')

        db.session.commit()  # Commit updates to the database
        return course

    @staticmethod
    def get_course_details(course_id: int) -> Optional[Course]:
        """Fetch a course details by ID including associated teacher information.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Optional[Course]: The course object or None if not found.
        """
        return Course.query.get(course_id)  # Retrieve course by ID

    @staticmethod
    def create_course_without_teacher(course_name: str) -> Course:
        """Create a new course without assigning a teacher.

        Args:
            course_name (str): The name of the course to be created.

        Returns:
            Course: The newly created course object.
        """
        course = Course(name=course_name)  # Teacher ID is not set
        db.session.add(course)
        db.session.commit()
        return course
```