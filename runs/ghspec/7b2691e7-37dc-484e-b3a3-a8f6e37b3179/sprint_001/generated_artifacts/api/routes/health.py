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