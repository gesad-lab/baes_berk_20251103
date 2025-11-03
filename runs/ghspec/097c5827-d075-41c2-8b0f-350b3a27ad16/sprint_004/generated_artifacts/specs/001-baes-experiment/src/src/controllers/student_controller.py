```python
# src/controllers/student_controller.py

from flask import Blueprint, request, jsonify
from http import HTTPStatus
from src.models import Student, Course  # Assuming these are defined in models.py
from src.services.student_service import (
    link_courses_to_student,
    retrieve_student_courses,
)
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

student_blueprint = Blueprint('student', __name__)

class LinkCoursesSchema(Schema):
    """Schema for validating linking courses to students."""
    course_ids = fields.List(fields.Int(required=True), required=True)

@student_blueprint.route('/students/<int:id>/courses', methods=['POST'])
def link_courses(id):
    """Link courses to a student.

    Args:
        id (int): The ID of the student.

    Returns:
        JSON response containing updated student details or error message.
    """
    # Validate the incoming request data
    try:
        data = request.get_json()
        validated_data = LinkCoursesSchema().load(data)
    except ValidationError as err:
        return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": err.messages}}), HTTPStatus.BAD_REQUEST

    try:
        student = link_courses_to_student(id, validated_data['course_ids'])
        return jsonify(student), HTTPStatus.OK
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Invalid student ID or course IDs"}}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": {"code": "E003", "message": str(e)}}), HTTPStatus.INTERNAL_SERVER_ERROR


@student_blueprint.route('/students/<int:id>/courses', methods=['GET'])
def get_student_courses(id):
    """Retrieve the courses linked to a specific student.

    Args:
        id (int): The ID of the student.

    Returns:
        JSON response with student's courses or error message.
    """
    try:
        courses = retrieve_student_courses(id)
        return jsonify(courses), HTTPStatus.OK
    except ValueError:
        return jsonify({"error": {"code": "E004", "message": "Student not found"}}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({"error": {"code": "E005", "message": str(e)}}), HTTPStatus.INTERNAL_SERVER_ERROR
```