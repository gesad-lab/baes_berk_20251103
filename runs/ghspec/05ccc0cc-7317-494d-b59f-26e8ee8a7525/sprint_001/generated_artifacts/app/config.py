```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify that the application is running.

    Returns:
        JSON response indicating the application status.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```