```python
# src/services.py

from models import Course, Teacher  # Import existing models
from typing import Optional
from sqlalchemy.orm import Session

class CourseService:
    """Service class to manage course-related operations, including teacher assignments."""

    def __init__(self, session: Session):
        self.session = session

    def assign_teacher_to_course(self, course_id: int, teacher_id: int) -> bool:
        """
        Assign a teacher to a course if the teacher exists.

        Parameters:
            course_id (int): The ID of the course to which the teacher should be assigned.
            teacher_id (int): The ID of the teacher to assign.

        Returns:
            bool: True if the teacher was assigned successfully, else False.
        """
        course = self.session.query(Course).filter_by(id=course_id).first()
        teacher = self.session.query(Teacher).filter_by(id=teacher_id).first()

        if not teacher:
            raise ValueError(f"E404: Teacher with ID {teacher_id} does not exist.")

        if course:
            course.teacher_id = teacher_id  # Assign the teacher
            self.session.commit()  # Commit changes to the database
            return True
        return False

    def validate_teacher_exists(self, teacher_id: int) -> bool:
        """
        Validate if a teacher exists in the database.

        Parameters:
            teacher_id (int): The ID of the teacher to validate.

        Returns:
            bool: True if the teacher exists, else False.
        """
        teacher = self.session.query(Teacher).filter_by(id=teacher_id).first()
        return teacher is not None
```