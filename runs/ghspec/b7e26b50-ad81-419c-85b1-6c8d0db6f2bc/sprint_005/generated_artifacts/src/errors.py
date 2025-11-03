```python
# src/errors.py

from flask import jsonify

def handle_missing_name_error():
    """Handles the error scenario when the 'name' field is missing during teacher creation."""
    response = {
        "error": {
            "code": "E400",
            "message": "Name is required.",
            "details": {
                "field": "name",
                "message": "Please provide a valid name for the teacher."
            }
        }
    }
    return jsonify(response), 400

def handle_duplicate_email_error():
    """Handles the error scenario when a duplicate email is provided during teacher creation."""
    response = {
        "error": {
            "code": "E409",
            "message": "Email must be unique.",
            "details": {
                "field": "email",
                "message": "A teacher with this email already exists."
            }
        }
    }
    return jsonify(response), 409
```