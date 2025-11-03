```python
from flask import jsonify, request, abort
from src.models import Course  # Assuming a Course model exists in models.py
from src.repositories import CourseRepository  # Assuming a CourseRepository exists
from sqlalchemy.exc import IntegrityError

@app.route('/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    """
    Enroll a student in courses.

    Request Body:
    - course_ids (list): List of course IDs to enroll the student in.
    
    Returns:
    - 201 Created on success
    - 400 Bad Request if validation fails
    - 404 Not Found if the student or course does not exist
    - 500 Internal Server Error on unexpected errors
    """
    json_data = request.get_json()

    # Validation: Check if course_ids is provided and is a list
    if not json_data or 'course_ids' not in json_data or not isinstance(json_data['course_ids'], list):
        return jsonify({"error": {"code": "E001", "message": "Invalid input: 'course_ids' is required and must be a list."}}), 400

    # Check if all course IDs are integers
    course_ids = json_data['course_ids']
    if not all(isinstance(course_id, int) for course_id in course_ids):
        return jsonify({"error": {"code": "E002", "message": "Invalid input: All course IDs must be integers."}}), 400

    try:
        # Attempt to enroll the student
        CourseRepository.enroll_student(student_id, course_ids)  # Assuming this method exists

    except IntegrityError:
        # Handles case where student or course does not exist
        return jsonify({"error": {"code": "E003", "message": "Student or course not found."}}), 404

    except Exception as e:
        # Log the detailed error
        app.logger.error(f"Unexpected error occurred while enrolling student: {str(e)}")
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred. Please try again later."}}), 500

    return jsonify({"message": "Student successfully enrolled in courses."}), 201


@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """
    Retrieve a student's enrolled courses.

    Returns:
    - 200 OK with the list of courses if found
    - 404 Not Found if the student does not exist
    - 500 Internal Server Error on unexpected errors
    """
    try:
        courses = CourseRepository.get_student_courses(student_id)  # Assuming this method exists
        if courses is None:
            return jsonify({"error": {"code": "E004", "message": "Student not found."}}), 404

    except Exception as e:
        # Log the detailed error
        app.logger.error(f"Unexpected error occurred while retrieving courses for student {student_id}: {str(e)}")
        return jsonify({"error": {"code": "E500", "message": "An unexpected error occurred. Please try again later."}}), 500

    return jsonify(courses), 200
```