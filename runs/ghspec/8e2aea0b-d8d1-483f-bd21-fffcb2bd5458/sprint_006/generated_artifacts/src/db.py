```python
# src/db.py

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Teacher, Course

# Initialize the database engine
engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)

def assign_teacher_to_course(course_id: int, teacher_id: int) -> dict:
    """
    Assign a teacher to an existing course.
    
    Parameters:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher to assign to the course.
    
    Returns:
        dict: A confirmation message or error information.
    """
    session = Session()
    response = {}

    try:
        # Check if the course exists
        course = session.query(Course).filter(Course.id == course_id).first()
        if not course:
            response = {
                "error": {
                    "code": "E002",
                    "message": "Course not found.",
                    "details": {"course_id": course_id}
                }
            }
            return response, 404
        
        # Check if the teacher exists
        teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            response = {
                "error": {
                    "code": "E003",
                    "message": "Teacher not found.",
                    "details": {"teacher_id": teacher_id}
                }
            }
            return response, 404

        # If both course and teacher exist, assign the teacher to the course
        course.teacher_id = teacher.id
        session.commit()
        
        response = {
            "message": "Teacher assigned successfully.",
            "course_id": course.id,
            "teacher_id": teacher.id,
            "teacher_name": teacher.name
        }
        return response, 200

    except IntegrityError as e:
        session.rollback()
        response = {
            "error": {
                "code": "E004",
                "message": "Database integrity error.",
                "details": str(e.orig)  # Specific database error message
            }
        }
        return response, 400

    finally:
        session.close()
```