```python
from flask import Flask, jsonify, request
from src.services import get_student_courses, enroll_student_in_course
from src.models import db
from src.database import init_db

app = Flask(__name__)

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def retrieve_student_courses(student_id):
    """Retrieve all courses associated with a specific student."""
    try:
        courses = get_student_courses(student_id)  # Fetch student's courses from the service
        return jsonify(courses), 200  # Return the courses as JSON with a 200 OK status
    except ValueError as e:
        # Handle case where the student does not exist
        return jsonify({"error": {"code": "E001", "message": str(e), "details": {}}}), 404
    except Exception as e:
        # For any other unexpected errors, log and return a generic error response
        app.logger.error(f"Failed to retrieve courses for student {student_id}: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Internal server error", "details": {}}}), 500

@app.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student(student_id):
    """Enroll a student in a course by course_id."""
    course_data = request.json  # Get the JSON data from the request
    course_id = course_data.get('course_id')

    if not course_id:
        return jsonify({"error": {"code": "E003", "message": "course_id is required", "details": {}}}), 400

    try:
        enrollment = enroll_student_in_course(student_id, course_id)  # Enroll the student in the course
        return jsonify(enrollment), 201  # Return the enrollment confirmation with a 201 Created status
    except ValueError as e:
        # Handle common validation errors (e.g., invalid student or course)
        return jsonify({"error": {"code": "E001", "message": str(e), "details": {}}}), 400
    except Exception as e:
        # For any unexpected errors, log and return a generic error response
        app.logger.error(f"Failed to enroll student {student_id} in course {course_id}: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "Internal server error", "details": {}}}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
```