```python
from flask import Blueprint, jsonify
from src import db

# Create a blueprint for the health check
health_check_bp = Blueprint('health_check', __name__)

@health_check_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify that the service is running.

    Returns:
        jsonify: A JSON response indicating the health status of the service.
    """
    try:
        # You may want to include additional checks (e.g., checking the database connection)
        return jsonify(status="healthy"), 200
    except Exception as e:
        # Log the detailed error for debugging purposes (not shown here)
        # return error response with internal error status
        return jsonify(error={"code": "E500", "message": "Internal Server Error"}), 500

# Remember to register the blueprint in your main application file.
```