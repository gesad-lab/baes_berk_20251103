```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from fastapi import HTTPException
from .models import Course, Teacher
from .database import SessionLocal

# Updating the Course model to include a teacher_id foreign key
def create_tables():
    # Assuming the current SQLAlchemy Base instance is available in models.py
    Course.__table__.add_column(Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))

def assign_teacher_to_course(course_id: int, teacher_id: int):
    """Assign a teacher to a course."""
    db = SessionLocal()
    try:
        course = db.query(Course).filter(Course.id == course_id).one_or_none()
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")

        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).one_or_none()
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found")

        # Associate teacher with the course
        course.teacher_id = teacher_id
        db.commit()
        db.refresh(course)  # Refresh to get the latest state of the course

        return course  # Return updated course object

    except Exception as e:
        db.rollback()  # Rollback changes if something goes wrong
        raise HTTPException(status_code=500, detail="An error occurred while assigning the teacher")
    finally:
        db.close()  # Ensure the database session is closed
```