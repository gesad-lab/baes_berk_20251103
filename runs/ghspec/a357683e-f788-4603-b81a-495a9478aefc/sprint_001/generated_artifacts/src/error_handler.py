from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, message):
        self.message = message


@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the application."""
    # Handle HTTP exceptions first
    if isinstance(e, HTTPException):
        return jsonify({"error": {
            "code": "HTTP_ERROR",
            "message": e.description
        }}), e.code

    # Handle custom validation errors
    if isinstance(e, ValidationError):
        return jsonify({"error": {
            "code": "VALIDATION_ERROR",
            "message": e.message
        }}), 400

    # For any unhandled exceptions, return a generic error message
    return jsonify({"error": {
        "code": "INTERNAL_SERVER_ERROR",
        "message": "An unexpected error occurred."
    }}), 500

# Example function to demonstrate usage of the error handler
@app.route('/students', methods=['POST'])
def create_student():
    """
    Example endpoint for creating a student.
    This should include validation according to the specification.
    """
    data = {"name": "Sample Student"}  # Simulated request data for illustration

    # Simulate validation logic
    if 'name' not in data or not data['name']:
        raise ValidationError("The 'name' field is required.")

    # Proceed with creating the student...
    return jsonify({"message": "Student created successfully."}), 201

if __name__ == "__main__":
    app.run(debug=True)