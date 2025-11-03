```python
# src/repositories/student_repository.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse

class StudentRepository:
    """Repository to handle database operations related to students and their course associations."""

    def __init__(self, db: Session):
        """Initialize the repository with a database session."""
        self.db = db

    def associate_course_with_student(self, student_id: int, course_id: int) -> None:
        """Associate a course with a student.

        Args:
            student_id (int): The ID of the student to associate the course with.
            course_id (int): The ID of the course to associate with the student.

        Raises:
            ValueError: If the student or course does not exist.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        course = self.db.query(Course).filter(Course.id == course_id).first()

        if not student:
            raise ValueError(f"E001: Student with ID {student_id} does not exist.")
        if not course:
            raise ValueError(f"E002: Course with ID {course_id} does not exist.")

        # Create a new association in the pivot table
        association = StudentCourse(student_id=student.id, course_id=course.id)
        self.db.add(association)
        self.db.commit()

    def get_student_with_courses(self, student_id: int) -> Optional[dict]:
        """Retrieve a student's details along with their associated courses.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Optional[dict]: A dictionary containing student details and their courses, or None if not found.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None 

        # Retrieve associated courses
        courses = self.db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
        return {
            'student': {
                'id': student.id,
                'name': student.name
                # Add any additional student fields if needed
            },
            'courses': [{'id': course.id, 'name': course.name} for course in courses]
        }
```