```python
# src/services/course_service.py

from flask import jsonify
from your_app import db  # make sure to replace with actual import paths
from src.models import Course, Teacher  # ensure proper model imports
from sqlalchemy.exc import NoResultFound

def assign_teacher_to_course(course_id: int, teacher_id: int) -> dict:
    """Assign a teacher to a course by updating the course's teacher_id.

    Args:
        course_id (int): The unique identifier for the course.
        teacher_id (int): The unique identifier for the teacher.

    Returns:
        dict: Confirmation of the teacher assignment or error message.
    """
    try:
        # Retrieve the course by ID
        course = Course.query.filter_by(id=course_id).one()  # Raises NoResultFound if not found
        # Update the course's teacher_id
        course.teacher_id = teacher_id
        db.session.commit()
        return {
            "message": "Teacher assigned successfully",
            "course_id": course.id,
            "teacher_id": teacher_id
        }
    except NoResultFound:
        # Handle the case where the course does not exist
        return {"error": {"code": "E001", "message": "Course not found"}}, 404
    except Exception as e:
        # General exception to handle unexpected errors
        db.session.rollback()  # Rollback the session on error
        return {"error": {"code": "E002", "message": str(e)}}, 500

def get_course_details(course_id: int) -> dict:
    """Retrieve the details of a course along with its assigned teacher.

    Args:
        course_id (int): The unique identifier for the course.

    Returns:
        dict: Course details including teacher information or error message.
    """
    try:
        # Retrieve the course with the teacher relationship
        course = Course.query.filter_by(id=course_id).one()  # Raises NoResultFound if not found
        teacher = Teacher.query.get(course.teacher_id)  # Get the assigned teacher

        # Build the response data
        response_data = {
            "course_id": course.id,
            "course_name": course.name,
            "teacher": {
                "teacher_id": teacher.id,
                "teacher_name": teacher.name
            } if teacher else None  # Include teacher details if available
        }
        return response_data
    except NoResultFound:
        # Handle the case where the course does not exist
        return {"error": {"code": "E001", "message": "Course not found"}}, 404
    except Exception as e:
        # General exception to handle unexpected errors
        return {"error": {"code": "E002", "message": str(e)}}, 500
```