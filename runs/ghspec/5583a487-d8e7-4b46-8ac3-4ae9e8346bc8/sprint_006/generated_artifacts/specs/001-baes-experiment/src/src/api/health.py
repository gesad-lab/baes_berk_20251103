```python
from flask import jsonify, request
from app import app, db
from app.models import Course, Teacher  # Import the Course and Teacher models

@app.route('/health', methods=['GET'])
def health_check():
    """Health Check Endpoint.

    Returns a simple message to verify that the API is up and running.
    """
    try:
        # A simple check to see if the database can be queried
        db.session.execute('SELECT 1')  # This can also be a simple query to a table if needed
        return jsonify({"status": "healthy", "message": "API is running."}), 200
    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Health check failed: {e}")
        return jsonify({"status": "unhealthy", "message": "Database is down or unreachable."}), 500
```