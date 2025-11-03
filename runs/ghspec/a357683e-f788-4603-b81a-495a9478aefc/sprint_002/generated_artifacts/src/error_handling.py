```python
# src/error_handling.py

import json
from email_validator import validate_email, EmailNotValidError

def handle_error(error):
    """
    Centralized error handler to format error messages for the API.
    
    Parameters:
        error (Exception): The raised exception to handle.

    Returns:
        str: JSON formatted error response to be sent to the client.
    """
    response = {}
    if isinstance(error, EmailNotValidError):
        # Handle email validation errors specifically
        response['error'] = {
            'code': 'E001',
            'message': 'Invalid email format',
            'details': str(error)
        }
    else:
        # General error response for other exceptions
        response['error'] = {
            'code': 'E002',
            'message': 'An unexpected error occurred',
            'details': str(error)
        }
    
    # Log the error details here if needed (not implemented for brevity)
    
    return json.dumps(response), 400  # Return JSON response with a 400 status for client errors

def validate_student_email(email):
    """
    Validate the provided email address.

    Parameters:
        email (str): The email address to validate.

    Raises:
        EmailNotValidError: If the email is not valid according to the validation rules.
    """
    try:
        # Validate the email, this will raise an EmailNotValidError if the email is invalid
        valid = validate_email(email)
        return valid.email  # Return the normalized email
    except EmailNotValidError as e:
        # Reraise the exception for global error handler to catch
        raise e
```