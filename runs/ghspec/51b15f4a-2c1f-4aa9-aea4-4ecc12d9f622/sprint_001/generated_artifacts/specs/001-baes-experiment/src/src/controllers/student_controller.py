from flask import Blueprint, request, jsonify
from models.student import Student
from schemas.student_schema import StudentSchema
from database import db

student_controller = Blueprint('student_controller', __name__)
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@student_controller.route('/students', methods=['POST'])
def add_student():
    """Endpoint to add a new student.

    Request body should contain:
    - name (string): The name of the student

    Returns:
    - JSON response with created student's data or an error message.
    """
    json_data = request.get_json()

    # Validate input data
    errors = student_schema.validate(json_data)
    if errors:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": errors}}), 400

    # Create and add new student to the database
    new_student = Student(name=json_data['name'])

    try:
        db.session.add(new_student)
        db.session.commit()
    except Exception as e:
        # Log error for debugging and return a user-friendly error message
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Failed to add student", "details": str(e)}}), 500

    return jsonify(student_schema.dump(new_student)), 201

@student_controller.route('/students', methods=['GET'])
def get_students():
    """Endpoint to retrieve all students.

    Returns:
    - JSON response with a list of students' data.
    """
    try:
        students = Student.query.all()
        return jsonify(students_schema.dump(students)), 200
    except Exception as e:
        # Log error for debugging
        return jsonify({"error": {"code": "E003", "message": "Failed to retrieve students", "details": str(e)}}), 500