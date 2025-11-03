from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health Check Endpoint

    Returns the status of the API.

    Response:
        200 OK: API is running smoothly.
        500 Internal Server Error: API is not operational.

    Example Response:
    {
        "status": "ok"
    }
    """
    return jsonify({"status": "ok"}), 200

@health_bp.route('/email-examples', methods=['GET'])
def email_examples():
    """
    Email Validation Example Endpoint

    Provides examples of valid and invalid email formats for reference.

    Response:
        200 OK with examples of valid and invalid email addresses.
    
    Example Response:
    {
        "valid_emails": [
            "john.doe@example.com",
            "jane.doe123@domain.co",
            "user.name+tag@sub.domain.com"
        ],
        "invalid_emails": [
            "john.doe@.com",         # Missing domain name
            "john.doe@com",          # Missing top-level domain
            "johndoe@com.",          # Trailing dot in domain
            "@missingusername.com",   # Missing username
            "plainaddress"           # No @ symbol
        ]
    }
    """
    examples = {
        "valid_emails": [
            "john.doe@example.com",
            "jane.doe123@domain.co",
            "user.name+tag@sub.domain.com"
        ],
        "invalid_emails": [
            "john.doe@.com",         # Missing domain name
            "john.doe@com",          # Missing top-level domain
            "johndoe@com.",          # Trailing dot in domain
            "@missingusername.com",   # Missing username
            "plainaddress"           # No @ symbol
        ]
    }
    return jsonify(examples), 200