```python
from flask import Blueprint, request, jsonify
from models import Student, db  # Assuming these are defined in models.py
from sqlalchemy.exc import IntegrityError

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.

    Request example:
    {
      "name": "John Doe"
    }
    
    Returns:
    - 201 Created with student details on success
    - 400 Bad Request if 'name' is missing
    """

    # Get JSON data from request
    data = request.get_json()
    
    # Validate input (check if 'name' is present)
    if 'name' not in data or not data['name']:
        return jsonify({
            "error": {
                "code": "E001",
                "message": "Missing required field: name"
            }
        }), 400  # 400 Bad Request
    
    # Create and save the student record
    new_student = Student(name=data['name'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({
            "id": new_student.id,
            "name": new_student.name
        }), 201  # 201 Created
    except IntegrityError:
        # Handle case for duplicate entries or database errors
        db.session.rollback()  # Rollback the session on error
        return jsonify({
            "error": {
                "code": "E003",
                "message": "Database error occurred. Please try again."
            }
        }), 500  # 500 Internal Server Error

@students_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    """
    Retrieve a student record by its identifier.

    Returns:
    - 200 OK with student details on success
    - 404 Not Found if the student does not exist
    """
    
    student = Student.query.get(id)
    if not student:
        return jsonify({
            "error": {
                "code": "E002",
                "message": "Student not found"
            }
        }), 404  # 404 Not Found
    
    return jsonify({
        "id": student.id,
        "name": student.name
    }), 200  # 200 OK
```