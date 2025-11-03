```python
from flask import Flask, request, jsonify, abort
from models import db, Course, StudentCourses
from services.student_course_service import associate_courses_with_student, get_courses_for_student

app = Flask(__name__)

@app.route('/api/v1/students/<int:student_id>/courses', methods=['POST'])
def associate_courses(student_id):
    """
    Associate multiple courses with a specific student.

    Parameters:
        student_id (int): The ID of the student to whom courses will be associated.
    
    Request Body:
        {
            "course_ids": [1, 2, 3]  # List of course IDs to be associated
        }
    
    Returns:
        A JSON response with a success message or error details.
    """
    data = request.get_json()
    course_ids = data.get('course_ids', [])

    if not isinstance(course_ids, list) or not all(isinstance(id, int) for id in course_ids):
        # Invalid input format, return error if course_ids is not a list of integers
        return jsonify({"error": {"code": "E001", "message": "Invalid course IDs provided. Must be a list of integers."}}), 400

    try:
        # Call the service layer to handle the association
        associate_courses_with_student(student_id, course_ids)
        return jsonify({"message": "Courses successfully associated with student."}), 200
    except ValueError as ve:
        # Handle specific value errors (e.g., non-existent course IDs)
        return jsonify({"error": {"code": "E002", "message": str(ve)}}), 400
    except Exception as e:
        # General error handler for unexpected issues
        return jsonify({"error": {"code": "E003", "message": "An unexpected error occurred.", "details": str(e)}}), 500


@app.route('/api/v1/students/<int:student_id>/courses', methods=['GET'])
def fetch_student_courses(student_id):
    """
    Retrieve courses associated with a specific student.

    Parameters:
        student_id (int): The ID of the student whose courses will be fetched.

    Returns:
        A JSON response containing a list of courses or an error message.
    """
    try:
        courses = get_courses_for_student(student_id)
        return jsonify(courses), 200
    except ValueError as ve:
        # Handle specific value errors, such as student not found
        return jsonify({"error": {"code": "E004", "message": str(ve)}}), 404
    except Exception as e:
        # General error handler for unexpected issues
        return jsonify({"error": {"code": "E005", "message": "An unexpected error occurred.", "details": str(e)}}), 500

if __name__ == '__main__':
    app.run(debug=True)
```