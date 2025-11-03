```python
# src/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models.student import Student
from src.models.course import Course
from src.models.student_courses import StudentCourses  # New import for the junction table
from src.api.student_api import student_api  # Assuming student_api is where the endpoints will be defined

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Adjust to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register blueprints for the API
app.register_blueprint(student_api)

# Initialize the database
def init_db():
    """Initializes the database with the necessary tables, including the junction table."""
    with app.app_context():
        db.create_all()  # This will create all tables defined in the models
        # Additional code can go here to check for existing data and manage initial setup.

if __name__ == "__main__":
    init_db()  # This will run the initialization
    app.run(debug=True)
```