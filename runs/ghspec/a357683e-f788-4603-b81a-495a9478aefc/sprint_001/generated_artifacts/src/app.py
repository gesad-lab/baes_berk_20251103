from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create Flask application instance
app = Flask(__name__)

# Set up configuration for the database (assuming SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a simple route for health check
@app.route('/')
def health_check():
    return jsonify({"status": "healthy"}), 200

# Import routes and models here (to avoid circular imports)
# from .models import Student  # Example import
# from .routes import student_routes  # Example import

# Register routes
# app.register_blueprint(student_routes)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set to False in production environments

# Note: Error handling and routing for CRUD operations will be implemented in separate modules as detailed in the technical plan.