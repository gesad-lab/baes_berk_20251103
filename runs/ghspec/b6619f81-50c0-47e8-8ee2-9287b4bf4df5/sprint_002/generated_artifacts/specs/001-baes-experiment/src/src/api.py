from flask import Flask, request, jsonify
from models import Student  # Assuming Student model is defined in models.py
from repositories import student_repository  # Assuming repository for database interaction
from sqlalchemy.exc import IntegrityError
import logging

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student with a name and email.

    Request Body:
    - name (string): The name of the student (required)
    - email (string): The email of the student (required)

    Returns:
    - 201 Created on success with student data.
    - 400 Bad Request if name or email is missing or invalid.
    """
    data = request.get_json()

    # Validate required fields
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required fields."}}), 400

    name = data['name']
    email = data['email']

    # Create the student
    try:
        new_student = Student(name=name, email=email)
        student_repository.save(new_student)  # Assume this handles the DB save and commit
        return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Email already exists."}}), 400
    except Exception as e:
        logging.error(f"Error creating student: {str(e)}")
        return jsonify({"error": {"code": "E003", "message": "An internal error occurred."}}), 500


@app.route('/students', methods=['GET'])
def retrieve_students():
    """
    Retrieve all students.

    Returns:
    - 200 OK with a list of students.
    """
    students = student_repository.get_all()  # Assume this method retrieves all student records
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200


@app.route('/students/<int:student_id>', methods=['GET'])
def retrieve_student(student_id):
    """
    Retrieve a specific student by id.

    Returns:
    - 200 OK with student data if found.
    - 404 Not Found if student does not exist.
    """
    student = student_repository.get_by_id(student_id)  # Assume this method retrieves a student by ID
    if not student:
        return jsonify({"error": {"code": "E004", "message": "Student not found."}}), 404

    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """
    Update an existing student.

    Request Body:
    - name (string): The updated name of the student (required)
    - email (string): The updated email of the student (required)

    Returns:
    - 200 OK with updated student data.
    - 400 Bad Request if name or email is missing or invalid.
    - 404 Not Found if student does not exist.
    """
    data = request.get_json()

    # Validate required fields
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and email are required fields."}}), 400

    name = data['name']
    email = data['email']

    # Update the student
    student = student_repository.get_by_id(student_id)
    if not student:
        return jsonify({"error": {"code": "E004", "message": "Student not found."}}), 404

    try:
        student.name = name
        student.email = email
        student_repository.save(student)  # Persist the changes
        return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200
    except IntegrityError:
        return jsonify({"error": {"code": "E002", "message": "Email already exists."}}), 400
    except Exception as e:
        logging.error(f"Error updating student: {str(e)}")
        return jsonify({"error": {"code": "E003", "message": "An internal error occurred."}}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)