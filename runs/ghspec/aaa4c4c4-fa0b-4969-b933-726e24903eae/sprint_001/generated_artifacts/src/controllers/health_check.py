from flask import Blueprint, jsonify

# Create a Blueprint for the health check
health_check_bp = Blueprint('health_check', __name__)

@health_check_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health Check Endpoint.

    Returns:
        JSON response with status 200 to indicate the API is up and running.
    """
    response = {
        "status": "OK",
        "message": "API is healthy"
    }
    return jsonify(response), 200

# Register the blueprint in the main application (this should be done in the app's initialization code)
# app.register_blueprint(health_check_bp)