from flask import Flask, jsonify
from src.database import db
from src.config import Config

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Create the database schema on startup
    with app.app_context():
        try:
            db.create_all()  # Create database tables
            print("Database schema created successfully.")
        except Exception as e:
            print(f"Error creating database schema: {e}")

    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint for monitoring."""
        return jsonify({"status": "healthy"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)