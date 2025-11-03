from flask import Blueprint, request, jsonify
from models import Student, db

student_api = Blueprint('student_api', __name__)

@student_api.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student.
    Request Body:
        - name (string): The name of the student (required).
    Response:
        - 201 Created with the created student record.
        - 400 Bad Request if the name field is empty.
    """
    data = request.json

    # Validate input
    if not data or 'name' not in data or not data['name'].strip():
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Name field is required"
            }
        }), 400

    new_student = Student(name=data['name'])

    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name}), 201

@student_api.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a student by ID.
    Response:
        - 200 OK with the student record in JSON format.
        - 404 Not Found if the student does not exist.
    """
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    return jsonify({"id": student.id, "name": student.name}), 200

@student_api.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update an existing student's name.
    Request Body:
        - name (string): The new name of the student (required).
    Response:
        - 200 OK with the updated student record.
        - 404 Not Found if the student does not exist.
        - 400 Bad Request if the name field is empty.
    """
    data = request.json
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    # Validate input
    if not data or 'name' not in data or not data['name'].strip():
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Name field is required"
            }
        }), 400

    student.name = data['name']
    db.session.commit()

    return jsonify({"id": student.id, "name": student.name}), 200

@student_api.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """
    Delete a student by ID.
    Response:
        - 204 No Content if the deletion is successful.
        - 404 Not Found if the student does not exist.
    """
    student = Student.query.get(student_id)

    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

    db.session.delete(student)
    db.session.commit()

    return '', 204