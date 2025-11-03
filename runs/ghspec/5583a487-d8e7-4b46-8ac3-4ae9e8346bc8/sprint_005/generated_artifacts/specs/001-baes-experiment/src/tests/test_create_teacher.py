```python
from flask import jsonify, request
from app import app, db
from app.models import Teacher  # Import the Teacher model

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new Teacher record.

    Request body must contain `name` (string) and `email` (string).
    Returns a confirmation message with status code 201 for success,
    or descriptive error messages with status code 400 for validation failures.
    """
    data = request.get_json()  # Parse the JSON request body
    
    # Validate that required fields are present
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": {"code": "E001", "message": "Missing required fields: name and email."}}), 400
    
    name = data['name']
    email = data['email']

    # Validate email format (basic validation, can be enhanced with regex)
    if not isinstance(email, str) or "@" not in email:
        return jsonify({"error": {"code": "E002", "message": "Invalid email format."}}), 400

    # Check for uniqueness of email in the database
    existing_teacher = Teacher.query.filter_by(email=email).first()
    if existing_teacher:
        return jsonify({"error": {"code": "E003", "message": "Email must be unique."}}), 400

    # Create the new Teacher record
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()  # Commit the transaction to save the new teacher

    return jsonify({"message": "Teacher created successfully.", "teacher": {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}}), 201
```