from flask import Blueprint, request, jsonify
from src.models import Student  # Assuming this is where your Student model is defined
from src.extensions import db  # Assuming this is where your db instance is defined

# Define a blueprint for student routes
student_blueprint = Blueprint('students', __name__)

@student_blueprint.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student.
    
    Request Body:
    {
        "name": "string"  // required
    }
    
    Responses:
    - 201 Created: Returns the newly created student.
    - 400 Bad Request: Returns error details for validation issues.
    """
    data = request.get_json()
    
    # Validate input
    if not data or 'name' not in data or not data['name'].strip():
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Name field is required.",
                "details": {}
            }
        }), 400

    # Create a new student instance
    new_student = Student(name=data['name'])
    
    # Add the student to the database
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "id": new_student.id,
        "name": new_student.name
    }), 201

@student_blueprint.route('/students', methods=['GET'])
def retrieve_students():
    """
    Retrieve all students.
    
    Responses:
    - 200 OK: Returns an array of students.
    - 500 Internal Server Error: Returns error if the database connection fails.
    """
    try:
        students = Student.query.all()
        return jsonify([{"id": student.id, "name": student.name} for student in students]), 200
    except Exception as e:
        # Log exception (not shown here for simplicity)
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Internal Server Error.",
                "details": str(e)
            }
        }), 500

# Register the blueprint in the main app (not shown here, usually done in app.py)