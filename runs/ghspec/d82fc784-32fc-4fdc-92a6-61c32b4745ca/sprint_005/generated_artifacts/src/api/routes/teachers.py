```python
from flask import Blueprint, request, jsonify
from app.models import Teacher
from app import db
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher record."""
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        logger.error("Invalid request data: %s", data)
        return jsonify({"error": {"code": "E001", "message": "Invalid input data"}}, 400)

    new_teacher = Teacher(name=data['name'], email=data['email'])
    db.session.add(new_teacher)
    db.session.commit()

    logger.info("Created teacher with email: %s", new_teacher.email)
    return jsonify(new_teacher.to_dict()), 201

@teachers_bp.route('/teachers', methods=['GET'])
def get_teachers():
    """Retrieve all teachers from the database."""
    teachers = Teacher.query.all()
    logger.info("Retrieved %d teachers", len(teachers))
    return jsonify([teacher.to_dict() for teacher in teachers]), 200

@teachers_bp.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    """Update an existing teacher's information."""
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        logger.error("Invalid update request data: %s", data)
        return jsonify({"error": {"code": "E001", "message": "Invalid input data"}}, 400)

    teacher = Teacher.query.get_or_404(teacher_id)
    teacher.name = data['name']
    teacher.email = data['email']
    db.session.commit()

    logger.info("Updated teacher with ID: %s, new email: %s", teacher_id, teacher.email)
    return jsonify(teacher.to_dict()), 200
```