```python
from flask import Blueprint, request, jsonify
from src.models import Student
from src.database import db_session

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student with the provided name.

    Request body should be a JSON object with a 'name' field.
    Returns the created student object or an error message.
    """
    data = request.get_json()

    # Validate the input: Ensure the 'name' field is present and not empty
    if not data or 'name' not in data or not data['name'].strip():
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Invalid input: name is required and cannot be empty.'
            }
        }), 400  # Bad Request

    new_student = Student(name=data['name'])

    try:
        db_session.add(new_student)
        db_session.commit()
        return jsonify(new_student.to_dict()), 201  # Created
    except Exception as e:
        db_session.rollback()
        return jsonify({
            'error': {
                'code': 'E002',
                'message': 'Failed to create student.',
                'details': str(e)
            }
        }), 500  # Internal Server Error

@student_routes.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all students from the database.

    Returns a JSON array of student objects.
    """
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200  # OK

```