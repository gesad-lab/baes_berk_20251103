```python
import json
import logging
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = 'sqlite:///students.db'
engine = create_engine(DATABASE_URL)

# Create a Session class
Session = sessionmaker(bind=engine)

# Custom error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return JSON error responses."""
    if isinstance(e, SQLAlchemyError):
        # Handle SQLAlchemy errors
        logging.error(f"Database error: {str(e)}")
        response = {
            "error": {
                "code": "DATABASE_ERROR",
                "message": "A database error occurred.",
                "details": str(e)
            }
        }
        return jsonify(response), 500
    
    # For other exceptions, log and return a generic error
    logging.error(f"Unexpected error: {str(e)}")
    response = {
        "error": {
            "code": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred."
        }
    }
    return jsonify(response), 500

# Initialize the database
def init_db():
    """Initialize the database and create tables if they do not exist."""
    try:
        with engine.begin() as connection:
            connection.execute("PRAGMA foreign_keys=ON")  # Enable foreign key constraints
            Base.metadata.create_all(engine)  # Create the tables
        logging.info("Database initialized successfully.")
    except SQLAlchemyError as e:
        logging.error(f"Error during database initialization: {str(e)}")
        raise

if __name__ == "__main__":
    init_db()  # Initialize the database on startup
    app.run(debug=True)  # Start the Flask application
```