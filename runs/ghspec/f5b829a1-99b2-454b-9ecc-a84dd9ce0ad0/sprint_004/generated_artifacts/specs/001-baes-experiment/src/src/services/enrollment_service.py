```python
# src/services/enrollment_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Enrollment, Student, Course

class EnrollmentService:
    """
    Service for managing student enrollments in courses.
    
    Responsibilities:
    - Enroll students in courses
    - Retrieve courses for a student
    """

    def __init__(self, db: Session):
        self.db = db

    def enroll_student(self, student_id: int, course_id: int):
        """
        Enroll a student into a course by creating an enrollment record.
        
        Parameters:
        - student_id (int): The ID of the student to enroll.
        - course_id (int): The ID of the course to enroll the student in.

        Returns:
        A dictionary containing student_id and course_id.

        Raises:
        HTTPException: If the student or course does not exist.
        """
        # Check if the student exists
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Check if the course exists
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        # Create enrollment record
        enrollment = Enrollment(student_id=student.id, course_id=course.id)
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)

        return {"studentId": enrollment.student_id, "courseId": enrollment.course_id}

    def get_courses_for_student(self, student_id: int):
        """
        Retrieve all courses that a student is enrolled in.
        
        Parameters:
        - student_id (int): The ID of the student whose courses are to be retrieved.

        Returns:
        A list of courses the student is enrolled in.

        Raises:
        HTTPException: If the student does not exist.
        """
        # Check if the student exists
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Retrieve courses for the student
        courses = self.db.query(Course).join(Enrollment).filter(Enrollment.student_id == student.id).all()

        return {"courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]}
```