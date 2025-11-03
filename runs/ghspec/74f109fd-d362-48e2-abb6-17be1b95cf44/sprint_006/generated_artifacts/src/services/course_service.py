```python
from repositories.course_repository import CourseRepository

class CourseService:
    """Encapsulates business logic for Course operations."""

    def __init__(self):
        self.course_repo = CourseRepository()

    def assign_teacher_to_course(self, course_id: int, teacher_id: int):
        """Assigns a teacher to the specified course.

        Args:
            course_id (int): The ID of the course to which the teacher will be assigned.
            teacher_id (int): The ID of the teacher to be assigned to the course.

        Returns:
            Course: The updated course instance with the assigned teacher or None if course is not found.
        """
        # Validate inputs
        if course_id <= 0 or teacher_id <= 0:
            raise ValueError("Invalid course_id or teacher_id. Both must be positive integers.")
        
        # Call the repository to assign the teacher to the course
        return self.course_repo.assign_teacher(course_id, teacher_id)

    def get_course_with_teacher(self, course_id: int):
        """Retrieves course details along with the assigned teacher.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            Course: The course instance with teacher details or None if course is not found.
        """
        # Validate input
        if course_id <= 0:
            raise ValueError("Invalid course_id. Must be a positive integer.")
        
        # Fetch course with teacher information from the repository
        return self.course_repo.get_course_with_teacher(course_id)
```