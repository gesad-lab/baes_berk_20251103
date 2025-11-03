```python
from flask import Blueprint, request, jsonify
from src.services.student_service import create_student, get_students
from werkzeug.exceptions import BadRequest, NotFound

# Create a Blueprint for the student related routes
student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['POST'])
def create_student_endpoint():
    """Endpoint to create a new student.
    
    Request Body:
        - name (str): The name of the student.
        - age (int): The age of the student.
        - email (str): The email of the student.
    
    Returns:
        JSON response with the created student data and HTTP status.
    """
    try:
        data = request.json
        # Validate incoming data
        if not data or 'name' not in data or 'age' not in data or 'email' not in data:
            raise BadRequest("Missing required fields: 'name', 'age', or 'email'.")

        student = create_student(data['name'], data['age'], data['email'])
        return jsonify(student), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while creating a student."}), 500

@student_bp.route('/students', methods=['GET'])
def retrieve_students_endpoint():
    """Endpoint to retrieve all students.
    
    Returns:
        JSON response with a list of student data and HTTP status.
    """
    try:
        students = get_students()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving students."}), 500
```