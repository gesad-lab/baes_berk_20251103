```python
from flask import jsonify, request
from app import app, db
from app.models import Course  # Assuming Course model is defined in app/models.py
import re

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new Course entry in the database.
    
    Expects a JSON body with 'name' and 'level' fields. Both fields are required.
    
    Returns:
        JSON response with the created Course details or an error message.
    """
    data = request.get_json()

    # Input validation and sanitization
    if 'name' not in data or not data['name'].strip():
        return jsonify({"error": {"code": "E001", "message": "The name field is required."}}), 400

    if 'level' not in data or not data['level'].strip():
        return jsonify({"error": {"code": "E002", "message": "The level field is required."}}), 400
    
    # Sanitize input to prevent XSS or similar issues
    sanitized_name = sanitize_input(data['name'])
    sanitized_level = sanitize_input(data['level'])

    # Create and add the new Course
    new_course = Course(name=sanitized_name, level=sanitized_level)
    db.session.add(new_course)
    db.session.commit()
    
    return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201

def sanitize_input(input_string: str) -> str:
    """Sanitize user input by stripping leading/trailing whitespace and escaping HTML entities.

    Args:
        input_string (str): The string to be sanitized.
        
    Returns:
        str: The sanitized string.
    """
    # Strip whitespace and escape HTML entities to prevent XSS
    return re.sub(r'&', '&amp;', re.sub(r'<', '&lt;', re.sub(r'>', '&gt;', input_string.strip())))
```