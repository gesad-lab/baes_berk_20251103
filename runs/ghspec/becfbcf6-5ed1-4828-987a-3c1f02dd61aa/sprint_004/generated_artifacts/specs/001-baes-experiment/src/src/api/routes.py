```python
from flask import jsonify
from app import app

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to monitor application status.

    Returns:
        JSON: A JSON object indicating the health status of the application
    """
    return jsonify({"status": "healthy"}), 200
```