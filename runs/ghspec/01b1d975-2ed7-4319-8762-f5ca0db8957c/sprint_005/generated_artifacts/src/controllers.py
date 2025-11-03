```python
from flask import Blueprint, request, jsonify
from src.models import db, Teacher
from src.validation import validate_teacher_creation

# Create a blueprint for the teacher routes
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher.

    Request must include the following JSON fields:
    - name: str (required)
    - email: str (required)

    Returns:
    - 201: Teacher created successfully with the new teacher's data.
    - 400: Bad request, validation errors.
    """
    data = request.get_json()

    # Validate the incoming data for teacher creation
    errors = validate_teacher_creation(data)
    if errors:
        return jsonify(errors), 400

    try:
        # Create a new Teacher instance
        new_teacher = Teacher(name=data['name'], email=data['email'])
        db.session.add(new_teacher)
        db.session.commit()

        return jsonify({
            'id': new_teacher.id,
            'name': new_teacher.name,
            'email': new_teacher.email
        }), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session on error
        return jsonify({'error': 'Failed to create teacher', 'details': str(e)}), 500

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve a teacher by their ID.

    Returns:
    - 200: Teacher data if found.
    - 404: Teacher not found.
    """
    teacher = Teacher.query.get(teacher_id)
    if teacher is None:
        return jsonify({'error': 'Teacher not found'}), 404

    return jsonify({
        'id': teacher.id,
        'name': teacher.name,
        'email': teacher.email
    }), 200
```