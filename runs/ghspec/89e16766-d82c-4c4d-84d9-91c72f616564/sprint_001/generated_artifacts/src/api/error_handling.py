from flask import jsonify

def create_error_response(error_code: str, error_message: str) -> dict:
    """
    Create a standardized error response format.
    
    Parameters:
        error_code (str): A code representing the error type.
        error_message (str): A descriptive error message for the user.

    Returns:
        dict: A standardized error response containing the error code and message.
    """
    return jsonify({"error": {"code": error_code, "message": error_message}}), 400

def handle_validation_error(validation_errors: dict) -> dict:
    """
    Handle validation errors and create a structured error response.

    Parameters:
        validation_errors (dict): A dictionary of validation errors.

    Returns:
        dict: A standardized error response including the validation details.
    """
    errors = []
    for field, messages in validation_errors.items():
        for message in messages:
            errors.append(f"{field}: {message}")
    return create_error_response("E001", "Validation errors occurred. " + "; ".join(errors))