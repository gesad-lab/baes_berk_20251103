```python
# src/services/course_service.py

from src.repositories.course_repository import CourseRepository
from src.models.course import Course
from src.models.teacher import Teacher
from sqlalchemy.exc import NoResultFound

class CourseService:
    """Service for managing courses and their relationships with teachers."""

    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def assign_teacher_to_course(self, course_id: int, teacher_id: int) -> Course:
        """Assign a teacher to a specified course.

        Args:
            course_id (int): The ID of the course to which the teacher will be assigned.
            teacher_id (int): The ID of the teacher to be assigned to the course.

        Returns:
            Course: The updated course object with the assigned teacher.

        Raises:
            ValueError: If the teacher ID is invalid or if the course does not exist.
        """
        # Validate that the course exists
        course = self.course_repository.get_course_by_id(course_id)
        if not course:
            raise ValueError(f"E001: Course with ID {course_id} does not exist.")

        # Check if the teacher exists (this could be another repository call)
        teacher = self.course_repository.get_teacher_by_id(teacher_id)  
        if not teacher:
            raise ValueError(f"E002: Teacher with ID {teacher_id} does not exist.")

        # Assign the teacher to the course
        course.teacher_id = teacher_id
        
        # Update the course in the repository
        self.course_repository.update_course(course)

        return course

    def get_course_with_teacher(self, course_id: int) -> Course:
        """Retrieve a course with its associated teacher's details.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The course object with teacher information.
        
        Raises:
            ValueError: If the course does not exist.
        """
        # Retrieve the course with teacher details from the repository
        course = self.course_repository.get_course_with_teacher(course_id)
        if not course:
            raise ValueError(f"E001: Course with ID {course_id} does not exist.")

        return course
```