```python
from flask import Blueprint, request, jsonify
from models.teacher import Teacher  # Assuming the Teacher model is in models/teacher.py
from database import session  # Assuming the database session is managed in database.py

teachers_bp = Blueprint('teachers', __name__)

def validate_teacher_data(name: str, email: str) -> None:
    """
    Validate the presence and format of teacher data.
    
    Parameters:
    - name (str): The name of the teacher.
    - email (str): The email of the teacher.
    
    Raises:
    - ValueError: If name or email is missing or if the email format is invalid.
    """
    if not name or not email:
        raise ValueError("Name and email are required.")
    
    # Basic email format validation (more comprehensive checks can be added)
    if '@' not in email:
        raise ValueError("Invalid email format.")

@teachers_bp.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    # Validate teacher data
    try:
        validate_teacher_data(data.get('name'), data.get('email'))
    except ValueError as e:
        return jsonify({"error": {"code": "E001", "message": str(e)}}), 400

    # Check for unique email
    existing_teacher = session.query(Teacher).filter_by(email=data['email']).first()
    if existing_teacher:
        return jsonify({"error": {"code": "E002", "message": "Email is already in use."}}), 409

    new_teacher = Teacher(name=data['name'], email=data['email'])
    session.add(new_teacher)
    session.commit()

    return jsonify({
        "message": "Teacher created successfully.",
        "teacher": {
            "id": new_teacher.id,
            "name": new_teacher.name,
            "email": new_teacher.email
        }
    }), 201
```