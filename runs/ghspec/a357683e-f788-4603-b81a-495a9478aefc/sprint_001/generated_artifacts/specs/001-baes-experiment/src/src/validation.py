import re
from flask import jsonify

def validate_student_name(name: str) -> bool:
    """Validate the student's name.

    Args:
        name (str): The name of the student to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Check if name is present and is a valid string
    if not name or not isinstance(name, str):
        return False
    
    # Check if name matches the acceptable character pattern (letters and spaces)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return False
    
    return True

def handle_validation_error(message: str) -> tuple:
    """Format validation error response.

    Args:
        message (str): The error message to include in response.

    Returns:
        tuple: A tuple containing the response data and the HTTP status code.
    """
    response = {
        "error": {
            "code": "E001",
            "message": message,
            "details": {}
        }
    }
    return jsonify(response), 400

def validate_create_student(data: dict) -> tuple:
    """Validate the incoming data for creating a student.

    Args:
        data (dict): The request data containing student information.

    Returns:
        tuple: A tuple containing the validation result and any error response.
    """
    name = data.get('name')
    
    if not validate_student_name(name):
        return False, handle_validation_error("Invalid name: Name must be a non-empty string containing only letters and spaces.")
    
    return True, None

def validate_update_student(data: dict) -> tuple:
    """Validate the incoming data for updating a student.

    Args:
        data (dict): The request data containing student information.

    Returns:
        tuple: A tuple containing the validation result and any error response.
    """
    if 'name' in data:
        return validate_create_student(data)
    return True, None

# Other validation functions can be added as needed for future extensions.