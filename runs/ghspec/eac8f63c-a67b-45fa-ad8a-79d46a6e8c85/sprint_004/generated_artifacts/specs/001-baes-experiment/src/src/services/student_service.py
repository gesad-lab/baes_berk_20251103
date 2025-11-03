```python
# src/services/student_service.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.student import Student
from models.student_course import StudentCourse
from models.course import Course

class StudentService:
    """Service for managing student-related operations."""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def associate_course_with_student(self, student_id: int, course_id: int) -> None:
        """
        Associate a course with a student.

        :param student_id: ID of the student to associate the course with.
        :param course_id: ID of the course to associate.
        :raises ValueError: If the provided course_id does not exist.
        :raises NoResultFound: If the student with the given ID does not exist.
        """
        # Validate that the course exists
        course = self.db_session.query(Course).filter(Course.id == course_id).one_or_none()
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")

        # Retrieve the student and associate with the course
        student = self.db_session.query(Student).filter(Student.id == student_id).one_or_none()
        if not student:
            raise NoResultFound(f"Student with ID {student_id} does not exist.")

        # Create a new StudentCourse association
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        self.db_session.add(student_course)
        self.db_session.commit()

    def get_student_courses(self, student_id: int) -> dict:
        """
        Retrieve a student's details including enrolled courses.

        :param student_id: ID of the student to retrieve.
        :raises NoResultFound: If the student with the given ID does not exist.
        :return: A dictionary containing student details and courses.
        """
        student = self.db_session.query(Student).filter(Student.id == student_id).one_or_none()
        if not student:
            raise NoResultFound(f"Student with ID {student_id} does not exist.")

        # Fetch associated courses
        courses = (
            self.db_session.query(Course)
            .join(StudentCourse)
            .filter(StudentCourse.student_id == student.id)
            .all()
        )

        return {
            "student_id": student.id,
            "student_name": student.name,
            "courses": [course.name for course in courses]
        }
```