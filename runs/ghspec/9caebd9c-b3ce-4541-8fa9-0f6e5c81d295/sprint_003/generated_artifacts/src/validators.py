```python
from flask import jsonify, request
from your_application import app, db
from api.models import Course  # Assuming Course model is defined in models.py
from api.validators import validate_course  # This should be implemented in validators.py


@app.route('/courses', methods=['POST'])
def create_course():
    """
    Create a new course with the provided name and level.
    Request Body: JSON containing {"name": "Course Name", "level": "Course Level"}
    Response: JSON with confirmation message and created course ID, or error message.
    """
    data = request.get_json()

    # Validate input data
    validation_error = validate_course(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400  # Bad Request if validation fails

    # Create new course object and save to the database
    new_course = Course(name=data["name"], level=data["level"])
    db.session.add(new_course)
    db.session.commit()

    return jsonify({"message": "Course created successfully", "course_id": new_course.id}), 201  # Created


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve the details of a specific course by its ID.
    Response: JSON object containing the name and level of the requested course.
    """
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found"}}), 404  # Not Found

    return jsonify({"name": course.name, "level": course.level}), 200  # OK
```