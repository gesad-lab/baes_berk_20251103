```python
from flask import Blueprint, jsonify, abort
from models.course import Course  # Import the Course model
from models.teacher import Teacher  # Import the Teacher model
from database import session  # Import the database session

courses_controller = Blueprint('courses_controller', __name__)

@courses_controller.route('/courses/<int:course_id>', methods=['GET'])
def get_course_details(course_id):
    """
    Retrieve details of a specific Course including associated Teacher information.
    
    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        JSON: Course details including Teacher if found, otherwise error message.
    """
    
    # Attempt to retrieve the course by ID
    course = session.query(Course).filter(Course.id == course_id).first()

    # Check if the course exists
    if course is None:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Course not found."
            }
        }), 404

    # Prepare the response with course and associated teacher details
    teacher = session.query(Teacher).filter(Teacher.id == course.teacher_id).first()
    teacher_data = {"id": teacher.id, "name": teacher.name} if teacher else None

    return jsonify({
        "id": course.id,
        "name": course.name,
        "teacher": teacher_data
    }), 200
```