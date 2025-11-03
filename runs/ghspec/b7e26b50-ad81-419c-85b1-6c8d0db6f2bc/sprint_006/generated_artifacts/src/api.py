```python
from flask import Flask, request, jsonify, abort
from your_app import create_app, db  # Adjust import based on your app structure
from your_app.models import Student, Course, Teacher  # Import the Teacher model for validation

app = create_app()

# Centralized error handling for missing course data
@app.errorhandler(400)
def handle_bad_request(error):
    """Handles bad request errors with a standardized response format.

    Args:
        error (werkzeug.exceptions.BadRequest): The bad request error.

    Returns:
        json: A JSON response with error information.
    """
    response = {
        "error": {
            "code": "E400",
            "message": "Bad request",
        }
    }
    return jsonify(response), 400

@app.route('/courses/<int:id>', methods=['PATCH'])
def update_course(id):
    """Updates the specified course with new data.

    Args:
        id (int): The ID of the course to update.

    Returns:
        json: A JSON response indicating success or failure.
    """
    course = Course.query.get(id)  # Attempt to retrieve the course
    if course is None:
        abort(404)  # Course not found

    data = request.get_json()  # Parse incoming JSON data
    teacher_id = data.get('teacher_id')

    if teacher_id:
        # Validate if the provided teacher_id exists
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            abort(400, description='Invalid teacher ID')  # Return an error if the teacher does not exist

        # Assign the teacher to the course
        course.teacher_id = teacher_id

    db.session.commit()  # Commit the transaction

    return jsonify({"message": "Course updated successfully"}), 200
```