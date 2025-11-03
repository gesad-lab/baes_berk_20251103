```python
from flask import Flask, request, jsonify, abort
from your_app import db  # Adjust import based on your app structure
from your_app.models import Teacher  # Include the newly created Teacher model

app = Flask(__name__)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """
    Create a new teacher record.

    Request format:
    {
        "name": "string (required)",
        "email": "string (required, must be unique)"
    }

    Response format on success (201 Created):
    {
        "id": "integer",
        "name": "string",
        "email": "string"
    }

    Response format on error (400 Bad Request or 409 Conflict):
    {
        "error": {
            "code": "E400 or E409",
            "message": "Error message detailing the issue",
            "details": {}
        }
    }
    """
    # Get the request data
    data = request.get_json()

    # Validate request body
    if not data or 'name' not in data or 'email' not in data:
        abort(400, jsonify({
            "error": {
                "code": "E400",
                "message": "Bad request",
                "details": {"missing_fields": ["name", "email"]}
            }
        }))

    name = data['name'].strip()
    email = data['email'].strip()

    # Check for unique email
    existing_teacher = Teacher.query.filter_by(email=email).first()
    if existing_teacher:
        abort(409, jsonify({
            "error": {
                "code": "E409",
                "message": "Email must be unique",
                "details": {}
            }
        }))

    # Create new teacher record
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()

    # Return success response
    return jsonify({
        "id": new_teacher.id,
        "name": new_teacher.name,
        "email": new_teacher.email
    }), 201
```