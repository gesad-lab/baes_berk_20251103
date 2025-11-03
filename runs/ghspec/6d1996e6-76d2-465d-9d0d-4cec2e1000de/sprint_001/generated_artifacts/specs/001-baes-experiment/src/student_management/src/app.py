from flask import Flask, request, jsonify
from services.student import create_student, get_student, update_student, delete_student
from utils.validators import validate_student_name

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def add_student():
    """
    Endpoint to create a new student.
    
    Request Body:
    - name: str, required, the name of the student
    
    Returns:
    - 201: Student created successfully
    - 400: Bad request if name is invalid
    """
    data = request.get_json()
    student_name = data.get('name', '').strip()
    
    # Validate student name
    if not validate_student_name(student_name):
        return jsonify({"error": {"code": "E001", "message": "Invalid name: name cannot be empty."}}), 400

    try:
        new_student = create_student(student_name)
        return jsonify(new_student), 201
    except Exception as e:
        # Log the exception detail for debugging (not exposed to user)
        app.logger.error(f"Failed to create student: {str(e)}")
        return jsonify({"error": {"code": "E002", "message": "An error occurred while creating the student."}}), 500

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_info(student_id):
    """
    Endpoint to retrieve student information by ID.
    
    Parameters:
    - student_id: int, required, the ID of the student
    
    Returns:
    - 200: Student information retrieved successfully
    - 404: Student not found
    """
    try:
        student = get_student(student_id)
        if student is None:
            return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
        return jsonify(student), 200
    except Exception as e:
        app.logger.error(f"Error retrieving student: {str(e)}")
        return jsonify({"error": {"code": "E004", "message": "An error occurred while retrieving the student."}}), 500

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student_info(student_id):
    """
    Endpoint to update a student's name.
    
    Parameters:
    - student_id: int, required, the ID of the student
    
    Request Body:
    - name: str, required, new name for the student
    
    Returns:
    - 200: Student updated successfully
    - 400: Bad request if name is invalid
    - 404: Student not found
    """
    data = request.get_json()
    new_name = data.get('name', '').strip()
    
    if not validate_student_name(new_name):
        return jsonify({"error": {"code": "E001", "message": "Invalid name: name cannot be empty."}}), 400

    try:
        updated_student = update_student(student_id, new_name)
        if updated_student is None:
            return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
        return jsonify(updated_student), 200
    except Exception as e:
        app.logger.error(f"Failed to update student: {str(e)}")
        return jsonify({"error": {"code": "E005", "message": "An error occurred while updating the student."}}), 500

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student_info(student_id):
    """
    Endpoint to delete a student by ID.
    
    Parameters:
    - student_id: int, required, the ID of the student
    
    Returns:
    - 204: Student deleted successfully
    - 404: Student not found
    """
    try:
        if not delete_student(student_id):
            return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
        return '', 204
    except Exception as e:
        app.logger.error(f"Failed to delete student: {str(e)}")
        return jsonify({"error": {"code": "E006", "message": "An error occurred while deleting the student."}}), 500

if __name__ == '__main__':
    app.run(debug=True)