```python
# src/services/course_service.py

from sqlalchemy.exc import NoResultFound
from src.models.course import Course  # Assuming the Course model is defined here
from src.models.teacher import Teacher  # Assuming the Teacher model is defined here
from src import db  # Importing db instance for database operations
from src.exceptions import ValidationError  # Custom exception for validation errors

class CourseService:

    @staticmethod
    def assign_teacher(course_id: int, teacher_id: int) -> Course:
        """
        Assign a teacher to a course by linking the Course ID with the Teacher ID.

        Args:
            course_id (int): The ID of the course to which the teacher will be assigned.
            teacher_id (int): The ID of the teacher to be assigned.

        Raises:
            ValidationError: If the course or teacher does not exist.

        Returns:
            Course: The course with the assigned teacher.
        """
        course = Course.query.get(course_id)
        if not course:
            raise ValidationError(f"Course with ID {course_id} does not exist.")

        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise ValidationError(f"Teacher with ID {teacher_id} does not exist.")

        # Assign the teacher to the course
        course.teacher_id = teacher_id
        db.session.commit()
        return course

    @staticmethod
    def update_teacher(course_id: int, new_teacher_id: int) -> Course:
        """
        Update the teacher assigned to an existing course.

        Args:
            course_id (int): The ID of the course for which the teacher is being updated.
            new_teacher_id (int): The ID of the new teacher to assign to the course.

        Raises:
            ValidationError: If the course or new teacher does not exist.

        Returns:
            Course: The course with the updated teacher.
        """
        course = Course.query.get(course_id)
        if not course:
            raise ValidationError(f"Course with ID {course_id} does not exist.")

        new_teacher = Teacher.query.get(new_teacher_id)
        if not new_teacher:
            raise ValidationError(f"Teacher with ID {new_teacher_id} does not exist.")

        # Update the teacher for the course
        course.teacher_id = new_teacher_id
        db.session.commit()
        return course

    @staticmethod
    def get_course_with_teacher(course_id: int) -> Course:
        """
        Retrieve course details including the assigned teacher’s information.

        Args:
            course_id (int): The ID of the course to retrieve.

        Raises:
            ValidationError: If the course does not exist.

        Returns:
            Course: The course with the associated teacher's information.
        """
        course = Course.query.get(course_id)
        if not course:
            raise ValidationError(f"Course with ID {course_id} does not exist.")

        return course  # Assuming course object has the teacher relationship set up

```