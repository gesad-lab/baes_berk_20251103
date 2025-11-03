```python
from models.student_courses import StudentCourses  # Import the StudentCourses mapping model
from models.student import Student  # Import Student model
from models.course import Course  # Import Course model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

class EnrollmentService:
    """Service to handle operations related to student enrollments in courses."""

    @staticmethod
    def enroll_student(student_id: int, course_id: int) -> None:
        """
        Enroll a student in a specific course.
        
        Args:
            student_id (int): The ID of the student to enroll.
            course_id (int): The ID of the course to enroll the student in.
        
        Raises:
            ValueError: If either the student or course does not exist.
            IntegrityError: If the enrollment already exists.
        """
        # Validate that the student and course exist
        student = Student.query.get(student_id)
        course = Course.query.get(course_id)

        if not student:
            raise ValueError("E001: Invalid student ID, student does not exist.")
        if not course:
            raise ValueError("E002: Invalid course ID, course does not exist.")

        # Create the relationship if it doesn't already exist
        enrollment = StudentCourses(student_id=student_id, course_id=course_id)
        
        try:
            db.session.add(enrollment)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("E003: Enrollment already exists for this student and course.")

    @staticmethod
    def remove_student_from_course(student_id: int, course_id: int) -> None:
        """
        Remove the enrollment of a student from a specific course.
        
        Args:
            student_id (int): The ID of the student to unenroll.
            course_id (int): The ID of the course to remove the student from.
        
        Raises:
            ValueError: If either the student or course does not exist,
                         or if no enrollment exists for the student in the course.
        """
        # Validate that the student and course exist
        student = Student.query.get(student_id)
        course = Course.query.get(course_id)

        if not student:
            raise ValueError("E001: Invalid student ID, student does not exist.")
        if not course:
            raise ValueError("E002: Invalid course ID, course does not exist.")

        # Check for existing enrollment
        enrollment = StudentCourses.query.filter_by(student_id=student_id, course_id=course_id).first()
        if not enrollment:
            raise ValueError("E004: No enrollment found for this student in the specified course.")

        db.session.delete(enrollment)
        db.session.commit()

    @staticmethod
    def get_student_courses(student_id: int) -> list:
        """
        Retrieve all courses that a specific student is enrolled in.
        
        Args:
            student_id (int): The ID of the student whose courses to retrieve.
        
        Returns:
            list: A list of courses that the student is enrolled in.
        
        Raises:
            ValueError: If the student does not exist.
        """
        # Validate that the student exists
        student = Student.query.get(student_id)
        if not student:
            raise ValueError("E001: Invalid student ID, student does not exist.")

        # Retrieve courses associated with the student
        enrollments = StudentCourses.query.filter_by(student_id=student_id).all()
        return [enrollment.course for enrollment in enrollments]
```