```python
"""
app.py

This module serves as the main entry point for the Flask application, defining the API routes
and initializing the application.

Functional API Endpoints:
1. Create Teacher:
   - POST /teachers
   - Request Body:
     - name: string (required)
     - email: string (required)
   - Response:
     On Success: HTTP 201 Created with JSON body confirming creation with Teacher's ID.
     On Failure: HTTP 400 Bad Request with validation error details for missing fields.

2. Retrieve Teacher Details:
   - GET /teachers/{teacher_id}
   - Response:
     On Success: HTTP 200 OK with JSON object containing Teacher's ID, name, and email address.
     On Failure: HTTP 404 Not Found if the Teacher does not exist.

This module also handles any necessary database migrations related to the Teacher entity, ensuring
that the existing data for Students and Courses remains intact.

Purpose:
The addition of the Teacher entity allows for managing teacher data within the educational application,
enabling functionalities such as course assignments, teacher-student interactions, and reporting of
teaching staff, ultimately improving organizational efficiency in educational environments.

Usage:
Ensure proper configuration before running the app. Migrations should be applied to maintain
database integrity.
"""

from flask import Flask
# Additional imports
from src.routes import register_routes

def create_app(config_filename=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Load configuration
    if config_filename:
        app.config.from_pyfile(config_filename)

    # Register routes
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```