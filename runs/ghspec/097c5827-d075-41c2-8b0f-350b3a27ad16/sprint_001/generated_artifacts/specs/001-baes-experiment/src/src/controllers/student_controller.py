```python
from flask import request, jsonify
from src.services.student_service import create_student_service
from sqlalchemy.exc import IntegrityError

def create_student():
    """
    Handles the creation of a new student.

    Request Body:
        - name (str): The name of the student (required)

    Returns:
        JSON response with the created student's ID and name on success (HTTP 201),
        or an error message on failure (HTTP 400).
    """
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or not isinstance(data['name'], str):
        return jsonify({"error": "E001: 'name' is required and must be a string."}), 400

    try:
        # Call the service to handle the student creation logic
        student = create_student_service(data['name'])
        
        return jsonify({"id": student.id, "name": student.name}), 201

    except IntegrityError as e:
        # Handle integrity errors, such as unique constraint violations
        return jsonify({"error": "E002: Integrity error occurred."}), 400
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Unexpected error occurred: {e}")
        return jsonify({"error": "E003: An unexpected error occurred."}), 500
```