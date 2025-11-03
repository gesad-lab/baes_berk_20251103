```python
from src.models import Teacher
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

def create_teacher():
    """Create a new teacher profile with provided name and email."""
    data = request.get_json()

    # Validate the input
    name = data.get('name')
    email = data.get('email')

    errors = {}
    if not name:
        errors['name'] = "Name is required."
    if not email:
        errors['email'] = "Email is required."
    elif '@' not in email:
        errors['email'] = "Invalid email format."

    if errors:
        return jsonify({"error": {"code": "E001", "message": "Validation errors", "details": errors}}), 400

    try:
        new_teacher = Teacher(name=name, email=email)
        # Assume db.session is managing the database session
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({
            "id": new_teacher.id,
            "name": new_teacher.name,
            "email": new_teacher.email
        }), 201  # HTTP 201 Created
    except IntegrityError:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({"error": {"code": "E002", "message": "Teacher with this email already exists."}}), 409

def get_teacher(teacher_id):
    """Retrieve details of a specific teacher by their ID."""
    teacher = Teacher.query.get(teacher_id)

    if teacher is None:
        return jsonify({"error": {"code": "E003", "message": "Teacher not found."}}), 404

    return jsonify({
        "id": teacher.id,
        "name": teacher.name,
        "email": teacher.email
    }), 200  # HTTP 200 OK
```