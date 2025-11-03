```python
from flask import Blueprint, request, jsonify
from src.models import Teacher  # assuming there is a Teacher model defined in models.py
from src.database import db  # assuming there is a db object for database operations

# Create a Blueprint for routes
routes = Blueprint('routes', __name__)

@routes.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher with the given name and email."""
    data = request.get_json()
    
    # Validate input data
    name = data.get('name')
    email = data.get('email')
    
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    
    if not email or not isinstance(email, str) or "@" not in email:
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400
    
    # Create a new Teacher instance
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)  # Add the teacher to the session
    db.session.commit()  # Commit the session to save the teacher
    
    return jsonify({"teacher": {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}}), 201

@routes.route('/teachers', methods=['GET'])
def get_teachers():
    """Retrieve all teachers."""
    teachers = Teacher.query.all()  # Query all teachers from the database
    teachers_data = [{"id": teacher.id, "name": teacher.name, "email": teacher.email} for teacher in teachers]
    
    return jsonify(teachers_data), 200
```