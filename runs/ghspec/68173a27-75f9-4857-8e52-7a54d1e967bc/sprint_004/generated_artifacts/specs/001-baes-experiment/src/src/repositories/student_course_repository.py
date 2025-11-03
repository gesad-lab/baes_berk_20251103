```python
# src/repositories/student_course_repository.py

from typing import List, Tuple
from sqlalchemy.orm import Session
from src.models.student_course import StudentCourses
from src.models.student import Student
from src.models.course import Course
from sqlalchemy.exc import NoResultFound

class StudentCourseRepository:
    """Data Access Layer for managing Student-Course relationships."""

    def __init__(self, session: Session):
        self.session = session

    def enroll_student_in_courses(self, student_id: int, course_ids: List[int]) -> None:
        """
        Enroll a student in a list of courses.

        Parameters:
            student_id (int): The ID of the student to enroll.
            course_ids (List[int]): A list of course IDs to enroll the student in.

        Raises:
            ValueError: If any of the course IDs are invalid or the student does not exist.
        """
        # Validate that the student exists
        student = self.session.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")

        # Validate course IDs and prepare to enroll
        valid_courses = self.session.query(Course.id).filter(Course.id.in_(course_ids)).all()
        valid_course_ids = [course.id for course in valid_courses]
        
        invalid_course_ids = set(course_ids) - set(valid_course_ids)
        if invalid_course_ids:
            raise ValueError(f"Invalid course IDs: {', '.join(map(str, invalid_course_ids))}")

        # Enroll student in the valid courses
        for course_id in valid_course_ids:
            enrollment = StudentCourses(student_id=student_id, course_id=course_id)
            self.session.add(enrollment)
        self.session.commit()

    def retrieve_student_courses(self, student_id: int) -> Tuple[dict, List[int]]:
        """
        Retrieve a student's information along with their enrolled course IDs.

        Parameters:
            student_id (int): The ID of the student.

        Returns:
            Tuple[dict, List[int]]: A dictionary with student details and a list of enrolled course IDs.

        Raises:
            ValueError: If the student does not exist.
        """
        # Retrieve student details
        student = self.session.query(Student).filter(Student.id == student_id).one_or_none()
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        
        # Get enrolled course IDs
        enrolled_courses = self.session.query(StudentCourses).filter(StudentCourses.student_id == student_id).all()
        course_ids = [enrollment.course_id for enrollment in enrolled_courses]

        return {
            "student_id": student.id,
            "name": student.name,
            "enrolled_course_ids": course_ids
        }, course_ids
```
