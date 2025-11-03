```python
from flask import jsonify, request
from src.models import db, Student, Course  # Importing the database and models
from sqlalchemy.exc import NoResultFound

def get_student_courses(student_id):
    """
    Retrieve all courses a given student is enrolled in.

    Args:
        student_id (int): The ID of the student whose courses are to be retrieved.

    Returns:
        Response: JSON response containing the list of courses or error details.
    """
    try:
        # Fetch the student by ID
        student = db.session.query(Student).filter_by(id=student_id).one()
        
        # Retrieve enrolled courses
        courses = student.enrolled_courses
        
        # Create a list to hold course details
        course_details = [
            {
                "course_id": course.id,
                "name": course.name,
                "level": course.level
            }
            for course in courses
        ]

        return jsonify(course_details), 200  # Return the list of courses with HTTP 200 OK

    except NoResultFound:
        return jsonify({"error": {"code": "E404", "message": "Student not found."}}), 404  # Handle case where student not found
    except Exception as e:
        # Log the exception (not shown here for brevity) and return a generic error message
        return jsonify({"error": {"code": "E500", "message": "Internal server error."}}), 500  
```