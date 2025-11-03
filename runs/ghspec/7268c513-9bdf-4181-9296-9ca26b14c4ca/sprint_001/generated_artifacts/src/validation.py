```python
import json
from typing import Any, Dict, Tuple


def validate_student_creation_request(request_body: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
    """
    Validates the input for creating a new student record.

    Args:
        request_body (Dict[str, Any]): The request body containing student data.

    Returns:
        Tuple[bool, Dict[str, Any]]: A tuple containing a boolean indicating if the validation passed,
                                       and a dictionary containing error details if validation failed.
    """
    # Initialize validation response
    validation_errors = {}

    # Check for the 'name' field presence and value
    if 'name' not in request_body or not isinstance(request_body['name'], str) or not request_body['name'].strip():
        # Populate the error details
        validation_errors = {
            "error": {
                "code": "E001",
                "message": "Name is required."
            }
        }
        return False, validation_errors  # Validation failed

    # Validation passed
    return True, {}


def handle_request(request_body: str) -> str:
    """
    Handle the student creation request.

    Args:
        request_body (str): JSON string containing the student data.

    Returns:
        str: JSON response indicating the success or failure of the request.
    """
    # Parse the JSON request body
    try:
        parsed_request = json.loads(request_body)
    except json.JSONDecodeError:
        return json.dumps({"error": {"code": "E002", "message": "Invalid JSON format."}})

    # Validate the request
    is_valid, validation_response = validate_student_creation_request(parsed_request)
    
    if not is_valid:
        return json.dumps(validation_response)  # Return validation error response

    # Proceed with creating the student record (this part of the logic is assumed to be implemented)
    # Assuming successful insertion into database leads to:
    created_student = { "id": 1, "name": parsed_request['name'] }  # Dummy data for example

    # Return success response
    return json.dumps({"student": created_student}), 201


# Example usage
if __name__ == "__main__":
    # Simulate a request body
    request_json = '{"name": "John Doe"}'
    response = handle_request(request_json)
    print(response)  # Expected to print the successful creation response
```