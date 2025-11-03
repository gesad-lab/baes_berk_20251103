from flask import Blueprint, jsonify

# Create a Blueprint for health check
health_check_bp = Blueprint('health_check', __name__)

@health_check_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify if the service is running.

    Returns:
        JSON response indicating the service status.
    """
    return jsonify({"status": "healthy"}), 200