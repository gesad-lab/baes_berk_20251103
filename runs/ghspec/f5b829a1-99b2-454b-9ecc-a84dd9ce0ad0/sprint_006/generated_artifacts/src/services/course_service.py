```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from src.models.course import Course
from src.models.teacher import Teacher
from src.exceptions import NotFoundError

class CourseService:
    def __init__(self, db: Session):
        """Initialize CourseService with a database session."""
        self.db = db

    def assign_teacher(self, course_id: int, teacher_id: int):
        """Assign a teacher to a course by updating the course's teacher_id.

        Args:
            course_id (int): The ID of the course to update.
            teacher_id (int): The ID of the teacher to assign.

        Raises:
            NotFoundError: If the course or teacher does not exist.
        """
        course = self.db.query(Course).filter(Course.id == course_id).first()
        teacher = self.db.query(Teacher).filter(Teacher.id == teacher_id).first()

        if not course:
            raise NotFoundError(f"Course with ID {course_id} not found.")
        if not teacher:
            raise NotFoundError(f"Teacher with ID {teacher_id} not found.")

        course.teacher_id = teacher_id
        self.db.commit()
        return course

    def unassign_teacher(self, course_id: int):
        """Unassign the teacher from a course by setting the teacher_id to None.

        Args:
            course_id (int): The ID of the course to update.

        Raises:
            NotFoundError: If the course does not exist.
        """
        course = self.db.query(Course).filter(Course.id == course_id).first()

        if not course:
            raise NotFoundError(f"Course with ID {course_id} not found.")

        course.teacher_id = None  # Set the teacher_id to None to unassign
        self.db.commit()
        return course
```