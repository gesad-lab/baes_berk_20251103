```python
from flask import Blueprint, jsonify
from src.models import db, Teacher  # Import the Teacher model for DB queries

# Create a Blueprint for the routes
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/api/v1/teachers', methods=['GET'])
def retrieve_teachers():
    """
    Retrieve the list of all teachers including their names and emails.

    Returns:
        JSON response containing a list of teachers with name and email.
    """
    try:
        # Query all teachers from the database
        teachers = Teacher.query.all()
        # Format the response as a list of dictionaries
        teacher_list = [{"name": teacher.name, "email": teacher.email} for teacher in teachers]
        
        return jsonify(teacher_list), 200  # Successful retrieval
    except Exception as e:
        # Log the exception (consider implementing proper logging here)
        return jsonify({"error": {"code": "E500", "message": "Internal server error", "details": str(e)}}), 500

# Register the Blueprint in your Flask app (in app.py, not shown here)
```
