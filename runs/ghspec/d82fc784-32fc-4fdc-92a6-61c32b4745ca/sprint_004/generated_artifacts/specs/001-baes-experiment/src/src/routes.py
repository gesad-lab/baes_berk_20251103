from flask import Flask, jsonify, request
from app.models import db, Student, Course  # Assuming these models exist
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id):
    """
    Enroll a student in a specified course.

    Args:
        student_id (int): The ID of the student.
    
    Request Body:
        {
            "course_id": "Course ID"
        }

    Returns:
        Response: HTTP Status 201 Created on successful enrollment.
    """
    data = request.get_json()
    course_id = data.get("course_id")

    if not course_id:
        return jsonify({"error": {"code": "E001", "message": "Course ID is required."}}), 400

    # Enrollment logic (assumed)
    logger.info("Enrolling student %s in course %s.", student_id, course_id)
    # Here you would typically check if the student and course exist, and then create an enrollment record

    return jsonify({"message": "Student enrolled successfully."}), 201


@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    """
    Retrieve a list of courses a student is enrolled in.

    Args:
        student_id (int): The ID of the student.
    
    Returns:
        Response: A list of courses the student is enrolled in.
    """
    # Retrieve courses logic (assumed)
    logger.info("Retrieving courses for student %s.", student_id)
    # This should interact with your database to get the courses

    courses = []  # Replace with actual course fetching
    return jsonify(courses), 200

@app.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def unenroll_student_from_course(student_id, course_id):
    """
    Remove a student from a specified course.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.
    
    Returns:
        Response: HTTP Status 204 No Content on successful unenrollment.
    """
    logger.info("Unenrolling student %s from course %s.", student_id, course_id)
    # Unenrollment logic here...

    return '', 204

# Provide examples for request bodies and expected responses
@app.route('/api/examples', methods=['GET'])
def get_examples():
    """
    Provide examples for request bodies and expected responses.

    Returns:
        Response: A JSON containing example request bodies and expected responses.
    """
    examples = {
        "enroll_student": {
            "request": {
                "course_id": "CS101"
            },
            "expected_response": {
                "message": "Student enrolled successfully."
            }
        },
        "get_student_courses": {
            "expected_response": []
        },
        "unenroll_student": {
            "expected_response": None  # No content
        }
    }
    return jsonify(examples), 200

if __name__ == '__main__':
    app.run(debug=True)