```python
from flask import request, jsonify
from src.models import Teacher
from src.database import db

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher in the system."""
    data = request.get_json()
    
    # Validate request body for required fields
    if not data.get('name'):
        return jsonify({"error": {"code": "E001", "message": "Name is required."}}), 400
    if not data.get('email'):
        return jsonify({"error": {"code": "E002", "message": "Email is required."}}), 400

    # Creating a new Teacher instance and saving it to the database
    new_teacher = Teacher(name=data['name'], email=data['email'])
    db.session.add(new_teacher)
    db.session.commit()
    
    return jsonify({"message": "Teacher created successfully."}), 201
```