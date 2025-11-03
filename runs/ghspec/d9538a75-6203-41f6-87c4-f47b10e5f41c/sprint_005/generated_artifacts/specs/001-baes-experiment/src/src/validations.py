from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound
from your_application.models import Teacher  # Update with your actual import path

def validate_teacher_input(data):
    """
    Validate the input data for creating a new Teacher.

    Args:
        data (dict): The input data containing teacher details.

    Returns:
        tuple: A tuple containing a JSON response and HTTP status code.
    """
    # Check if 'name' is present and not empty
    if 'name' not in data or not data['name']:
        return jsonify({"error": {"code": "E001", "message": "Name is required"}}), 400
    
    # Check if 'email' is present and not empty
    if 'email' not in data or not data['email']:
        return jsonify({"error": {"code": "E002", "message": "Email is required"}}), 400
    
    # Validate email uniqueness
    try:
        existing_teacher = Teacher.query.filter_by(email=data['email']).one()
        return jsonify({"error": {"code": "E003", "message": "Email is already in use."}}), 400
    except NoResultFound:
        # No existing teacher with that email, proceed with validation
        pass

    return None  # Return None if validation passes (no errors)