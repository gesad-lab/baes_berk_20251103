```python
from flask import jsonify
from app import app

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for application monitoring.

    Returns:
        JSON response indicating the health status of the application.
    """
    return jsonify({"status": "healthy"}), 200
```