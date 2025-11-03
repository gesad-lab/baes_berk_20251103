```python
# src/services/course_service.py

from typing import List
from sqlalchemy.orm import Session
from models.course import Course  # Import Course model
from models.student_course import StudentCourse  # Import relationship model
from schemas.student_course_schemas import StudentCourseCreate, StudentCourseResponse  # Import schemas

class CourseService:
    """Service to manage Course operations related to Student enrollments."""

    def __init__(self, db: Session):
        """Initialize the CourseService with a database session.
        
        Args:
            db (Session): SQLAlchemy session for database operations.
        """
        self.db = db

    def enroll_student_in_course(self, student_id: int, course_id: int) -> StudentCourseResponse:
        """Enroll a student in a course.

        Args:
            student_id (int): The ID of the student to enroll.
            course_id (int): The ID of the course to enroll into.

        Returns:
            StudentCourseResponse: Details of the enrollment created.
        """
        # Create a new relationship entry for the student and course
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        self.db.add(student_course)  # Add the relationship to the session
        self.db.commit()  # Commit changes to the database
        self.db.refresh(student_course)  # Refresh to get the latest state

        return StudentCourseResponse.from_orm(student_course)  # Return the created enrollment details

    def remove_student_from_course(self, student_id: int, course_id: int) -> None:
        """Remove a student from a course.

        Args:
            student_id (int): The ID of the student to remove.
            course_id (int): The ID of the course to remove from.

        Returns:
            None
        """
        # Find the relationship entry for the student and course
        student_course = self.db.query(StudentCourse).filter_by(student_id=student_id, course_id=course_id).first()
        if student_course:
            self.db.delete(student_course)  # Delete the relationship from the session
            self.db.commit()  # Commit changes to the database

    def get_courses_for_student(self, student_id: int) -> List[Course]:
        """Retrieve a list of courses for a given student.

        Args:
            student_id (int): The ID of the student.

        Returns:
            List[Course]: List of courses the student is enrolled in.
        """
        # Query to get courses associated with the student
        return (
            self.db.query(Course)
            .join(StudentCourse)
            .filter(StudentCourse.student_id == student_id)
            .all()
        )
```