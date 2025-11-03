from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to monitor application status.
    
    Returns:
        JSON response with application status.
    """
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Start the application in debug mode for development
    app.run(debug=True)