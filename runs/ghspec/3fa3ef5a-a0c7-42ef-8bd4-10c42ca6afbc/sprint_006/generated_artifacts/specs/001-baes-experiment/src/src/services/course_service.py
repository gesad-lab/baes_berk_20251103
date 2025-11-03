```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from models.course import Course
from models.teacher import Teacher

class CourseService:
    """Service layer for managing course-related operations."""

    def __init__(self, session: Session):
        """Initialize CourseService with a database session."""
        self.session = session

    def assign_teacher_to_course(self, course_id: int, teacher_id: int) -> Course:
        """
        Assign a teacher to a course.

        Parameters:
        - course_id (int): The ID of the course to assign a teacher to.
        - teacher_id (int): The ID of the teacher to be assigned.

        Returns:
        - Course: The updated Course object with the assigned teacher.

        Raises:
        - ValueError: If the teacher does not exist.
        - Exception: For other database-related errors.
        """
        # Check if the teacher exists
        teacher = self.session.query(Teacher).get(teacher_id)
        if not teacher:
            raise ValueError(f"Teacher with ID {teacher_id} does not exist.")

        # Fetch the course to update
        course = self.session.query(Course).get(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")

        # Assign the teacher to the course
        course.teacher_id = teacher_id
        
        # Commit changes to the database
        self.session.commit()
        
        return course

    def remove_teacher_from_course(self, course_id: int) -> Course:
        """
        Remove the teacher from a course.

        Parameters:
        - course_id (int): The ID of the course to remove the teacher from.

        Returns:
        - Course: The updated Course object without the assigned teacher.

        Raises:
        - ValueError: If the course does not exist.
        - Exception: For other database-related errors.
        """
        # Fetch the course to update
        course = self.session.query(Course).get(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")

        # Remove the teacher assignment
        course.teacher_id = None
        
        # Commit changes to the database
        self.session.commit()
        
        return course
```