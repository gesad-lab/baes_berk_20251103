```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from models import Course, Teacher  # Assuming these models are defined in models.py
from fastapi import HTTPException

class CourseService:
    @staticmethod
    def assign_teacher(db: Session, course_id: int, teacher_id: int):
        """
        Assign a teacher to a course based on provided course_id and teacher_id.

        Args:
            db (Session): The SQLAlchemy database session.
            course_id (int): The ID of the course to update.
            teacher_id (int): The ID of the teacher to assign.

        Raises:
            HTTPException: If the course ID or teacher ID is invalid.

        Returns:
            Course: The updated course object.
        """
        # Validate course ID
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise HTTPException(status_code=404, detail="E001: Course ID is invalid")

        # Validate teacher ID
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher is None:
            raise HTTPException(status_code=404, detail="E002: Teacher ID is invalid")

        # Update the course with the new teacher ID
        course.teacher_id = teacher_id
        
        # Commit the changes to the database
        db.commit()
        db.refresh(course)  # Refresh the course instance to get updated data
        
        return course
```