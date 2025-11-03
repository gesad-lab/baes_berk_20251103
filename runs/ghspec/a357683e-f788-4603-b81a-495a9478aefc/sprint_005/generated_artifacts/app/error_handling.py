```python
# app/error_handling.py

from flask import jsonify

class ErrorResponse:
    """Handles error responses for the application."""

    @staticmethod
    def duplicate_email_error(email: str) -> tuple:
        """Return error response for duplicate email scenarios.
        
        Args:
            email (str): The duplicate email that was attempted to be registered.
        
        Returns:
            tuple: A tuple containing the error message and HTTP status code.
        """
        error_message = {
            "error": {
                "code": "E002",  # Custom error code for duplicate email
                "message": f"The email '{email}' is already associated with another teacher.",
                "details": {
                    "suggestion": "Please use a different email address."
                }
            }
        }
        return jsonify(error_message), 400  # Return HTTP 400 Bad Request

# Assuming an existing function that checks for duplicate emails
def validate_unique_email(email: str) -> None:
    """Validate that the email is unique before registration.
    
    Raises:
        ValueError: If the email is already in use.
    """
    if email_already_exists(email):  # Placeholder for the actual email validation check
        raise ValueError("Duplicate email")

# Adding the email validation in the context of creating a new teacher
def create_teacher(name: str, email: str) -> None:
    """Create a new teacher after validating input.
    
    Args:
        name (str): The name of the teacher.
        email (str): The email of the teacher.
    
    Raises:
        ValueError: If the email is already in use.
    """
    try:
        validate_unique_email(email)  # Validate email uniqueness
        # Logic to save the teacher in the database would go here
    except ValueError as e:
        # Handle error if duplicate email is found
        return ErrorResponse.duplicate_email_error(email)
```
