```python
from flask import Flask, request, jsonify, abort
from your_app import db  # Adjust import based on your app structure
from your_app.models import Student, Course  # Import relevant models
from your_app.errors import handle_error  # Import centralized error handler

app = Flask(__name__)

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """Fetch courses associated with a student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        JSON response containing a list of courses associated with the student or an error.
    """
    student = Student.query.get(student_id)
    if student is None:
        # Student not found, return 404 error
        abort(404, description="Student not found.")

    courses = student.courses  # Assuming a relationship exists in Student model
    courses_data = [{'id': course.id, 'name': course.name, 'level': course.level} for course in courses]

    return jsonify(courses_data), 200

@app.errorhandler(404)
def handle_not_found(error):
    """Handle not found errors with a JSON response.

    Args:
        error: The error raised.

    Returns:
        JSON response with error details.
    """
    response = {
        "error": {
            "code": "E404",
            "message": error.description,
        }
    }
    return jsonify(response), 404

if __name__ == '__main__':
    app.run(debug=True)
```