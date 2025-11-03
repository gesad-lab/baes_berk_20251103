```python
# src/services/course_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models import StudentCourse, Student, Course
from fastapi import HTTPException

class CourseService:
    """Service class for handling course enrollment and validation."""
    
    @staticmethod
    def enroll_student_in_course(db: Session, student_id: int, course_id: int) -> str:
        """Enroll a student in a course."""
        # Validate student and course existence
        student = db.query(Student).filter(Student.id == student_id).first()
        course = db.query(Course).filter(Course.id == course_id).first()
        
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        
        # Check if the student is already enrolled in the course
        existing_enrollment = db.query(StudentCourse).filter(
            StudentCourse.student_id == student_id,
            StudentCourse.course_id == course_id
        ).first()
        
        if existing_enrollment:
            raise HTTPException(status_code=400, detail="Student is already enrolled in this course")

        # Create new StudentCourse enrollment
        enrollment = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(enrollment)
        db.commit()

        return "Student enrolled successfully"

    @staticmethod
    def retrieve_student_courses(db: Session, student_id: int) -> List[Course]:
        """Retrieve all courses for a given student."""
        # Validate student existence
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Querying courses for the student
        courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
        return courses

    @staticmethod
    def remove_student_from_course(db: Session, student_id: int, course_id: int) -> str:
        """Remove a student from a course."""
        # Validate existence of student and course
        student = db.query(Student).filter(Student.id == student_id).first()
        course = db.query(Course).filter(Course.id == course_id).first()
        
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        
        # Find the existing enrollment
        enrollment = db.query(StudentCourse).filter(
            StudentCourse.student_id == student_id,
            StudentCourse.course_id == course_id
        ).first()
        
        if not enrollment:
            raise HTTPException(status_code=404, detail="Enrollment not found")

        # Remove the enrollment
        db.delete(enrollment)
        db.commit()

        return "Student removed from course successfully"
```
