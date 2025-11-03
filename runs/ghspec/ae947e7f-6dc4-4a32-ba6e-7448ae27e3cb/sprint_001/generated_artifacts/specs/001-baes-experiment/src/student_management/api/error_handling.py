```python
from flask import jsonify

class APIError(Exception):
    """Custom exception for API errors with structured responses."""
    def __init__(self, message: str, code: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code

def handle_api_error(error: APIError):
    """Handle API errors and return structured JSON response."""
    response = {
        "error": {
            "code": error.code,
            "message": error.message,
            "details": {}  # Additional details can be added here
        }
    }
    return jsonify(response), error.status_code

# General error handler for other exceptions
def handle_general_exception(error: Exception):
    """Handle general exceptions and return structured JSON response."""
    response = {
        "error": {
            "code": "E500",
            "message": "An unexpected error occurred.",
            "details": {
                "error": str(error)  # Log error message for debugging
            }
        }
    }
    return jsonify(response), 500

# Example Flask app snippet demonstrating error handling
from flask import Flask

app = Flask(__name__)

@app.errorhandler(APIError)
def api_error_handler(error: APIError):
    return handle_api_error(error)

@app.errorhandler(Exception)
def general_error_handler(error: Exception):
    return handle_general_exception(error)

# Example usage in a route
@app.route('/students', methods=['POST'])
def create_student():
    # Assume we have some logic here to extract parameters,
    # validate inputs, and create a student.
    try:
        # Simulate a raising APIError for demonstration
        raise APIError("Invalid name provided", "E001", 400)
    except APIError as e:
        return handle_api_error(e)

# The application must be run with a WSGI server for production
if __name__ == '__main__':
    app.run(debug=True)
```