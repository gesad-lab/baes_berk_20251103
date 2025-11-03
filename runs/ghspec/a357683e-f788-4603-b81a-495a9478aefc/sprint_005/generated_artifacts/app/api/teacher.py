```python
from flask import Blueprint, request, jsonify, abort
from app import db
from app.models import Teacher
from sqlalchemy.exc import IntegrityError

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    """Update Teacher Information

    Args:
        teacher_id (int): The ID of the teacher to update.

    Returns:
        JSON response with updated teacher information or error message.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": {"code": "E001", "message": "Invalid input data."}}), 400

    # Get the teacher by ID
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher not found."}}), 404

    # Validate email if provided
    email = data.get('email', None)
    if email:
        # Check if email is already in use by another teacher
        existing_teacher = Teacher.query.filter_by(email=email).first()
        if existing_teacher and existing_teacher.id != teacher_id:
            return jsonify({"error": {"code": "E003", "message": "Email already in use."}}), 400
        teacher.email = email

    # Update other fields as needed (currently only email is optional)
    # You could easily modify this section to allow updates to other teacher fields (like name)

    try:
        db.session.commit()
        return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
    except IntegrityError:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({"error": {"code": "E004", "message": "Database error occurred."}}), 500
```