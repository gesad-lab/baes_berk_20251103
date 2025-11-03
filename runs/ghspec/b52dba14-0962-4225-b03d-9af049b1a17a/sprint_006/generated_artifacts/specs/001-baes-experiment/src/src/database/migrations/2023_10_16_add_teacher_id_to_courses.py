```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update
import logging

# Setup the base model for the migration
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

def run_migration(engine):
    """Execute the migration to add teacher_id column to courses table."""
    with engine.begin() as connection:
        # Add the new teacher_id column
        connection.execute("""
        ALTER TABLE courses
        ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);
        """)
        logging.info("Migration executed: Added teacher_id to courses table.")

def assign_teacher_to_course(session, course_id, teacher_id):
    """Assign a teacher to a course specified by course_id."""
    try:
        stmt = update(Course).where(Course.id == course_id).values(teacher_id=teacher_id)
        result = session.execute(stmt)
        session.commit()
        if result.rowcount == 0:
            logging.warning(f"No course found with ID {course_id}. Teacher assignment not made.")
            return {"error": "Course not found"}, 404
        return {"message": "Teacher assigned successfully."}, 200
    except IntegrityError:
        logging.error(f"Failed to assign teacher_id {teacher_id} to course_id {course_id} due to integrity error.")
        session.rollback()
        return {"error": "Invalid teacher_id."}, 400
    except Exception as e:
        logging.error(f"Unexpected error during teacher assignment: {str(e)}")
        session.rollback()
        return {"error": "An unexpected error occurred."}, 500

def get_course_details(session, course_id):
    """Retrieve course details with teacher information."""
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        logging.warning(f"No course found with ID {course_id}.")
        return {"error": "Course not found."}, 404
        
    course_info = {
        "course_id": course.id,
        "name": course.name,
        "description": course.description,
        "teacher_id": course.teacher_id
    }
    return course_info, 200
```