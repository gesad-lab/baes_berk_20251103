```python
# src/services/student_course_service.py

from typing import List, Dict, Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models import Student, Course, StudentCourse  # Import all required models

class StudentCourseService:
    """Service for managing the enrollment of students in courses."""

    @staticmethod
    def enroll_student(db: Session, student_id: int, course_id: int) -> Dict[str, Any]:
        """Enroll a student in a course.

        Args:
            db (Session): The database session.
            student_id (int): The ID of the student to enroll.
            course_id (int): The ID of the course to enroll the student in.

        Raises:
            HTTPException: If the student or course does not exist or if already enrolled.

        Returns:
            Dict[str, Any]: A confirmation message indicating enrollment success.
        """
        student = db.query(Student).filter(Student.id == student_id).first()
        course = db.query(Course).filter(Course.id == course_id).first()

        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Student with ID {student_id} not found.")
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Course with ID {course_id} not found.")

        # Check if the student is already enrolled in the course
        if db.query(StudentCourse).filter(StudentCourse.student_id == student_id,
                                           StudentCourse.course_id == course_id).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Student is already enrolled in the specified course.")

        # Create student-course association
        enrollment = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(enrollment)
        db.commit()
        db.refresh(enrollment)  # Refresh to get the latest state of the object

        return {"message": "Enrollment successful", "enrollment": {"student_id": student_id, "course_id": course_id}}

    @staticmethod
    def get_enrolled_courses(db: Session, student_id: int) -> List[Dict[str, Any]]:
        """Get all courses a student is enrolled in.

        Args:
            db (Session): The database session.
            student_id (int): The ID of the student whose courses are to be retrieved.

        Raises:
            HTTPException: If the student does not exist.

        Returns:
            List[Dict[str, Any]]: A list of courses that the student is enrolled in.
        """
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Student with ID {student_id} not found.")

        enrolled_courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
        return [{"course_id": course.id, "name": course.name} for course in enrolled_courses]

    @staticmethod
    def remove_student_from_course(db: Session, student_id: int, course_id: int) -> Dict[str, Any]:
        """Remove a student from a course.

        Args:
            db (Session): The database session.
            student_id (int): The ID of the student to remove.
            course_id (int): The ID of the course to remove the student from.

        Raises:
            HTTPException: If the student or course does not exist or if the student isn't enrolled in the course.

        Returns:
            Dict[str, Any]: A confirmation message indicating removal success.
        """
        enrollment = db.query(StudentCourse).filter(StudentCourse.student_id == student_id,
                                                     StudentCourse.course_id == course_id).first()

        if not enrollment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="The student is not enrolled in the specified course.")

        db.delete(enrollment)
        db.commit()

        return {"message": "Student removed from course successfully"}
```