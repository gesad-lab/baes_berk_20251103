from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify that the application is running.

    Returns:
        JSON response indicating application health status.
    """
    # Respond with a simple success message
    response = {
        "status": "healthy",
        "message": "The application is running successfully."
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)