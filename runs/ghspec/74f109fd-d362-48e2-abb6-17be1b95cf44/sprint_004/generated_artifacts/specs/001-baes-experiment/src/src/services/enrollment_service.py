```python
# File: src/services/enrollment_service.py

from sqlalchemy.orm import sessionmaker
from models.student import Student
from models.course import Course
from models.student_courses import StudentCourses
from database import session
from repositories.student_courses_repository import StudentCoursesRepository
from fastapi import HTTPException

class EnrollmentService:
    """Service for managing student enrollments in courses."""

    def __init__(self, student_courses_repository: StudentCoursesRepository):
        self.student_courses_repository = student_courses_repository

    def enroll_student_in_course(self, student_id: int, course_id: int):
        """Enroll a student in a specific course by their IDs.

        Args:
            student_id (int): The ID of the student to enroll.
            course_id (int): The ID of the course in which to enroll the student.

        Raises:
            HTTPException: If the course or student does not exist.

        Returns:
            dict: A confirmation dictionary with student ID, course ID, and updated course list for the student.
        """
        # Validate student and course existence
        student = session.query(Student).filter_by(id=student_id).first()
        course = session.query(Course).filter_by(id=course_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found.")
        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")

        # Enroll student in the course
        self.student_courses_repository.enroll_student_in_course(student_id, course_id)

        # Retrieve updated course list for the student
        courses = [sc.course_id for sc in student.courses]
        return {"student_id": student_id, "course_id": course_id, "courses": courses}

    def enroll_student_in_multiple_courses(self, student_id: int, course_ids: list):
        """Enroll a student in multiple courses at once.

        Args:
            student_id (int): The ID of the student to enroll.
            course_ids (list): A list of course IDs in which to enroll the student.

        Raises:
            HTTPException: If any of the courses or student do not exist.

        Returns:
            dict: A confirmation dictionary with updated course list for the student.
        """
        # Validate student existence
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found.")

        # Ensure all course IDs are valid
        for course_id in course_ids:
            course = session.query(Course).filter_by(id=course_id).first()
            if not course:
                raise HTTPException(status_code=404, detail=f"Course {course_id} not found.")

            # Enroll the student in each valid course
            self.student_courses_repository.enroll_student_in_course(student_id, course_id)

        # Retrieve updated course list for the student
        courses = [sc.course_id for sc in student.courses]
        return {"student_id": student_id, "enrolled_courses": courses}

    def get_student_courses(self, student_id: int):
        """Retrieve all courses for a specific student by their ID.

        Args:
            student_id (int): The ID of the student to retrieve courses for.

        Raises:
            HTTPException: If the student does not exist.

        Returns:
            list: A list of courses the student is enrolled in.
        """
        # Validate student existence
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found.")

        # Get all courses the student is enrolled in
        courses = [sc.course_id for sc in student.courses]
        return {"student_id": student_id, "courses": courses}
```