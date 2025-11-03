```python
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from models import Student, Course, StudentCourses
from typing import List
from database import get_db  # Assuming a get_db function exists for database sessions

class StudentService:
    @staticmethod
    def assign_course_to_student(student_id: int, course_id: int, db: Session):
        """Assign a course to a student."""
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

        # Create a new relationship entry in the student_courses table
        student_course_entry = StudentCourses(student_id=student_id, course_id=course_id)
        db.add(student_course_entry)
        db.commit()
        db.refresh(student_course_entry)

        return {"message": "Course assigned successfully", "student_course": student_course_entry}

    @staticmethod
    def get_courses_for_student(student_id: int, db: Session) -> List[Course]:
        """Retrieve all courses for a specific student."""
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Query the relationship to get course details
        courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
        return courses
```