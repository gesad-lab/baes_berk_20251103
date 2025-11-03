from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy db instance
db = SQLAlchemy(app)

# Error handling for startup issues
@app.before_first_request
def create_database():
    """Create the database on startup if it does not exist."""
    try:
        db.create_all()
        print("Database created successfully.")
    except Exception as e:
        print(f"Error creating the database: {str(e)}")

# Import the routes after the app and db are initialized
from students import students_bp
app.register_blueprint(students_bp)

if __name__ == '__main__':
    # Start the application
    app.run(debug=True)