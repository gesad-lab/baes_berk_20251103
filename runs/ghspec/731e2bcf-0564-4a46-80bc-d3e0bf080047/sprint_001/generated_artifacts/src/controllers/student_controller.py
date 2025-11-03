```python
from flask import Blueprint, request, jsonify
from services.student_service import create_student, get_all_students

student_controller = Blueprint('student_controller', __name__)

@student_controller.route('/students', methods=['POST'])
def add_student():
    """
    Creates a new student record.
    
    Request JSON Format:
    {
        "name": "Student Name"
    }
    
    Returns:
        JSON response with message indicating success or failure.
    """
    data = request.get_json()
    
    # Validate input: Check if 'name' is provided and is not empty
    name = data.get('name')
    if not name or not isinstance(name, str):
        # Return error if 'name' is empty or not a string
        return jsonify({"error": {"code": "E001", "message": "Name field is required.", "details": {}}}), 400

    # Proceed to create the student if validation passes
    student = create_student(name)
    
    return jsonify({"message": "Student created successfully.", "student": student}), 201

@student_controller.route('/students', methods=['GET'])
def list_students():
    """
    Retrieves all student records.
    
    Returns:
        JSON response with a list of students, or an empty list if none exist.
    """
    students = get_all_students()
    return jsonify(students), 200
```