from flask import Blueprint, jsonify
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Create a Blueprint for health checks
health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the operational status of the application.

    Returns:
        JSON response indicating health status.
    """
    try:
        # Here you can add further checks (e.g., database connection)
        # For now we will simply return an 'OK' status
        response = {
            "status": "OK",
            "message": "The application is running smoothly."
        }
        return jsonify(response), 200
    except Exception as e:
        # Log error details for debugging
        logger.error("Health check failed: %s", e)
        return jsonify({
            "status": "ERROR",
            "message": "Health check failed",
            "details": str(e)
        }), 500 

# Note: Ensure this Blueprint is registered in your main application file.