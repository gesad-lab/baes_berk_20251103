```python
# src/services/teacher_service.py

from sqlalchemy.orm import Session
from models import Teacher, Course

class TeacherService:
    """Service for managing Teacher entities and their interactions with courses."""
    
    @staticmethod
    def assign_teacher_to_course(db: Session, course_id: int, teacher_id: int) -> Course:
        """
        Assign a teacher to a specific course.

        Args:
            db (Session): The database session.
            course_id (int): The ID of the course to which the teacher should be assigned.
            teacher_id (int): The ID of the teacher to assign to the course.

        Returns:
            Course: The updated Course object with the new teacher assignment.
        
        Raises:
            ValueError: If the course or teacher does not exist.
        """
        # Fetch the course from the database
        course = db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise ValueError(f"E002: Course with ID {course_id} does not exist.")
        
        # Fetch the teacher to ensure they exist
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher is None:
            raise ValueError(f"E003: Teacher with ID {teacher_id} does not exist.")
        
        # Assign the teacher to the course
        course.teacher_id = teacher_id
        
        # Commit the changes to the database
        db.commit()
        db.refresh(course)  # Refresh to get the latest state from the database
        
        return course
```