```python
from flask import Blueprint, request, jsonify
from api.models import Teacher, db
from sqlalchemy.exc import IntegrityError
import re

api = Blueprint('api', __name__)

# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@api.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher.

    This endpoint creates a new teacher with the provided name and email.
    Expects JSON body with 'name' and 'email'.
    Returns the created teacher object or error messages.
    """
    data = request.get_json()

    # Validate input data
    name = data.get('name')
    email = data.get('email')

    if not name or not isinstance(name, str):
        return jsonify({"error": {"code": "E001", "message": "Name is required and must be a string."}}), 400

    if not email or not re.match(EMAIL_REGEX, email):
        return jsonify({"error": {"code": "E002", "message": "A valid email is required."}}), 400

    # Create and persist the new teacher
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Teacher with this email already exists."}}), 400

    return jsonify({"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}), 201


@api.route('/teachers/<int:id>', methods=['GET'])
def get_teacher(id):
    """Retrieve a specific teacher by ID.

    This endpoint returns the teacher object associated with the provided ID.
    Returns the teacher's name and email or a not found error.
    """
    teacher = Teacher.query.get(id)
    
    if teacher is None:
        return jsonify({"error": {"code": "E004", "message": "Teacher not found."}}), 404

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200


@api.route('/teachers/<int:id>', methods=['PUT'])
def update_teacher(id):
    """Update an existing teacher.

    This endpoint updates the teacher's name and email based on provided data.
    Expects JSON body with optional 'name' and 'email'.
    Returns the updated teacher object or error messages.
    """
    data = request.get_json()
    
    # Attempt to find the teacher by ID
    teacher = Teacher.query.get(id)
    
    if teacher is None:
        return jsonify({"error": {"code": "E004", "message": "Teacher not found."}}), 404
    
    # Update fields if provided
    if 'name' in data:
        name = data['name']
        if not name or not isinstance(name, str):
            return jsonify({"error": {"code": "E001", "message": "Name is required and must be a string."}}), 400
        teacher.name = name

    if 'email' in data:
        email = data['email']
        if not email or not re.match(EMAIL_REGEX, email):
            return jsonify({"error": {"code": "E002", "message": "A valid email is required."}}), 400
        teacher.email = email

    # Commit the changes to the database
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Teacher with this email already exists."}}), 400

    return jsonify({"id": teacher.id, "name": teacher.name, "email": teacher.email}), 200
```