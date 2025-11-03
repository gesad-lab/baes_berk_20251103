```python
from flask import jsonify

def structured_error_response(code: str, message: str) -> dict:
    """
    Generate a structured error response for invalid requests.
    
    Args:
        code (str): The error code representing the type of error.
        message (str): A descriptive error message explaining the issue.

    Returns:
        dict: Structured error response in JSON format.
    """
    return jsonify({
        "error": {
            "code": code,
            "message": message
        }
    }), 400  # HTTP status code for Bad Request


# Example usage in a Flask view function
def create_student_endpoint():
    """API endpoint to create a new student record."""
    data = request.json
    if 'name' not in data or not data['name']:
        return structured_error_response("E001", "Name is required.")

    # Assuming further processing occurs here...
```
