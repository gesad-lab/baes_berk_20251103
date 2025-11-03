from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from environment variable or use default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///students.db")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Import models and routes to prevent circular imports
from models import Student  # Ensure `Student` model is defined here
import routes  # Import routes that register the API endpoints

def create_db():
    """Create the database and tables if they don't exist."""
    with app.app_context():
        db.create_all()  # Create database tables

if __name__ == "__main__":
    create_db()  # Setup the database at startup
    app.run(debug=True)  # Run the Flask app in debug mode