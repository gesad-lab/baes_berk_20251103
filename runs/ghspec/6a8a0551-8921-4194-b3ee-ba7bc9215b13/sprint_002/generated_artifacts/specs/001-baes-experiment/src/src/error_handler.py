```python
# src/error_handler.py

from flask import jsonify

def handle_validation_error(error_code: str, message: str):
    """Handles validation errors and formats a consistent error response.
    
    Args:
        error_code (str): The error code identifier for the error.
        message (str): A human-readable message explaining the error.
    
    Returns:
        tuple: Formatted JSON response and the HTTP status code.
    """
    response = {
        "error": {
            "code": error_code,
            "message": message,
            "details": {}
        }
    }
    return jsonify(response), 400

def handle_student_creation_error(validation_errors: dict):
    """Handles errors specific to student creation validations.
    
    Args:
        validation_errors (dict): A dictionary containing validation error details.
    
    Returns:
        tuple: Formatted JSON response and HTTP status code.
    """
    if 'email' in validation_errors:
        # Specific error for missing or invalid email
        email_error = validation_errors['email']
        return handle_validation_error("E002", email_error)

    # Handle other error scenarios (like name errors) if needed
    return handle_validation_error("E001", "Validation errors occurred.")

def handle_student_retrieval_error(student_id: int):
    """Handles errors related to student retrieval.
    
    Args:
        student_id (int): The ID of the student being retrieved.
    
    Returns:
        tuple: Formatted JSON response indicating not found error.
    """
    return handle_validation_error("E404", f"Student with ID {student_id} not found.")
```
