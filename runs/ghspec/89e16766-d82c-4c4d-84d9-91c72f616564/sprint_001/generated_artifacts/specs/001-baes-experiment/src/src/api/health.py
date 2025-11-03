from flask import Blueprint, jsonify

# Create a Blueprint for health check
health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    """Health Check Endpoint to confirm service availability."""
    try:
        return jsonify({"status": "ok", "message": "Service is healthy."}), 200
    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Health check failed: {str(e)}")
        return jsonify({"status": "error", "message": "Service is not healthy."}), 500

# Ensure the health check endpoint can be safely imported and registered in the main app
def register_health_check(app):
    """Registers the health check blueprint."""
    app.register_blueprint(health_bp)

