from flask import Blueprint, jsonify

# Create a blueprint for the health check endpoint
health_check_bp = Blueprint('health_check', __name__)

@health_check_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify server status.

    Returns:
        JSON: A simple message confirming that the server is running.
    """
    return jsonify({"status": "ok"}), 200