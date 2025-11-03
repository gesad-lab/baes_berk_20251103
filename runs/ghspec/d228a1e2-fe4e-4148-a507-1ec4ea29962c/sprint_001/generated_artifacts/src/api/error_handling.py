from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError

error_handling = Blueprint('error_handling', __name__)

# Error Handling for the API
@error_handling.errorhandler(400)
def handle_bad_request(error):
    return jsonify({"error": {"code": "E400", "message": "Bad Request"}}), 400

@error_handling.errorhandler(404)
def handle_not_found(error):
    return jsonify({"error": {"code": "E404", "message": "Not Found"}}), 404

@error_handling.errorhandler(IntegrityError)
def handle_integrity_error(error):
    return jsonify({"error": {"code": "E001", "message": "Database integrity error"}}), 400

@error_handling.errorhandler(Exception)
def handle_exception(error):
    # Log the error details here if needed
    return jsonify({"error": {"code": "E500", "message": "Internal Server Error"}}), 500

# Example function to create a student, showing how errors are handled
@error_handling.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return handle_bad_request(None)

    name = data['name']
    # Assume here we have a function to add student to the database
    try:
        student = add_student_to_database(name)  # Placeholder for actual DB logic
        return jsonify({"id": student.id, "name": student.name}), 201
    except IntegrityError:
        return handle_integrity_error(None)

# Example function to get a student by ID
@error_handling.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = get_student_from_database(id)  # Placeholder for actual DB logic
    if student is None:
        return handle_not_found(None)
       
    return jsonify({"id": student.id, "name": student.name}), 200

# Example function to list all students
@error_handling.route('/students', methods=['GET'])
def list_students():
    students = get_all_students_from_database()  # Placeholder for actual DB logic
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200