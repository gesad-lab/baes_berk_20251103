```python
from flask import Blueprint, jsonify, request
from src.models import Teacher  # Ensure the Teacher model is imported
from src.database import db  # Import the database instance to interact with it
from src.api.errors import handle_error  # Custom error handling function

# Create a Blueprint for the API routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher_details(teacher_id):
    """Fetches the details of a specific teacher by their ID.
    
    Args:
        teacher_id (int): The ID of the teacher to fetch.

    Returns:
        Response: A JSON representation of the teacher's details,
                  or an error message if the teacher is not found.
    """
    try:
        # Fetch the teacher from the database
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return handle_error(404, f"Teacher with ID {teacher_id} not found.")

        # Prepare the response data
        response_data = {
            'id': teacher.id,
            'name': teacher.name,
            'email': teacher.email
        }
        return jsonify(response_data), 200  # Return teacher details with a 200 OK status

    except Exception as e:
        # Handle any unexpected errors
        return handle_error(500, "An error occurred while fetching teacher details.")
```