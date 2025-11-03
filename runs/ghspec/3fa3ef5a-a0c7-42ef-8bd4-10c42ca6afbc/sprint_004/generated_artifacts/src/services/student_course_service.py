```python
# src/services/student_course_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse  # Assuming StudentCourse model is created
from fastapi import HTTPException

class StudentCourseService:
    """Service layer for managing student-course associations."""

    def __init__(self, db: Session):
        self.db = db

    def assign_courses_to_student(self, student_id: int, course_ids: List[int]) -> None:
        """
        Assign multiple courses to a student.

        Parameters:
        - student_id: ID of the student to associate courses with.
        - course_ids: List of course IDs to associate with the student.
        
        Raises:
        - HTTPException: If the student or any course does not exist.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        courses = self.db.query(Course).filter(Course.id.in_(course_ids)).all()
        if len(courses) != len(course_ids):
            raise HTTPException(status_code=404, detail="One or more courses not found")

        # Clear existing associations before adding new ones if required.
        student.courses.clear()  
        student.courses.extend(courses)  # Adding new courses

        self.db.commit()  # Persist changes to the database

    def remove_course_from_student(self, student_id: int, course_id: int) -> None:
        """
        Remove a specific course association from a student.

        Parameters:
        - student_id: ID of the student whose course association to remove.
        - course_id: ID of the course to be disassociated.
        
        Raises:
        - HTTPException: If the student or course does not exist.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        course = self.db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        if course in student.courses:
            student.courses.remove(course)  # Remove course from student's courses
            self.db.commit()  # Persist changes to the database
        else:
            raise HTTPException(status_code=400, detail="Course not associated with the student")

    def get_student_with_courses(self, student_id: int) -> Optional[Student]:
        """
        Retrieve a student alongside their associated courses.

        Parameters:
        - student_id: ID of the student to retrieve.

        Returns:
        - Student instance with associated courses or None if not found.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student  # Return the student instance (includes associated courses due to relationship)
```