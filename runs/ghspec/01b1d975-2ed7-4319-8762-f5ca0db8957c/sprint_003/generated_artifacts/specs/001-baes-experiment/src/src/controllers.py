```python
# src/controllers.py

from flask import jsonify, request
from your_project.models import Course  # Assuming the Course model will be created in models.py
from your_project import db  # Assuming SQLAlchemy is being used for database interactions
from your_project.validation import validate_course_data  # Add the validation function for course data

def create_course():
    """Create a new course in the database.

    Expects a JSON body with 'name' and 'level' fields.
    Returns JSON with course ID, name, and level on success, or error details on failure.
    """
    data = request.get_json()

    # Validate the input data
    validation_result = validate_course_data(data.get('name'), data.get('level'))
    if not validation_result['is_valid']:
        return jsonify({"errors": validation_result['errors']}), 400

    # Create a new Course object
    new_course = Course(name=data['name'], level=data['level'])
    
    # Add the new course to the database
    db.session.add(new_course)
    try:
        db.session.commit()
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except Exception as e:
        db.session.rollback()
        # Log the exception for debugging purposes (assuming logger is set up)
        # logger.error("Failed to create course: %s", e)
        return jsonify({"error": "Failed to create course. Please try again."}), 500


def retrieve_courses():
    """Retrieve all courses from the database.

    Returns a JSON array of courses, each containing ID, name, and level.
    On failure, returns a 500 error.
    """
    try:
        courses = Course.query.all()  # Query to get all courses
        courses_data = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
        return jsonify(courses_data), 200
    except Exception as e:
        # Log the exception for debugging purposes (assuming logger is set up)
        # logger.error("Failed to retrieve courses: %s", e)
        return jsonify({"error": "Failed to retrieve courses. Please try again later."}), 500
```