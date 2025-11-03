```python
from flask import Flask
from src.api.student_routes import student_blueprint
from src.api.enrollment_routes import enrollment_blueprint  # Importing new enrollment routes
from src.database import db

def create_app():
    app = Flask(__name__)
    
    # Initialize database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example configuration
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register blueprints for routing
    app.register_blueprint(student_blueprint)
    app.register_blueprint(enrollment_blueprint)  # Registering the new enrollment routes

    # Create the database tables, including the enrollment table
    with app.app_context():
        db.create_all()  # This will create all tables defined in models, including enrollments

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  # Set to False in production
```