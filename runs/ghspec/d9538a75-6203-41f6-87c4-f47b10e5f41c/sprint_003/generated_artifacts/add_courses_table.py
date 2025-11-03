```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Assuming the app and db have been initialized in your main application code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Existing Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)

# New Course model to represent the Course entity
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    name = db.Column(db.String, nullable=False)  # Required name field
    level = db.Column(db.String, nullable=False)  # Required level field

    def __init__(self, name: str, level: str):
        if not name:
            raise ValueError("Course name must not be empty")  # Validation for name
        if not level:
            raise ValueError("Course level must not be empty")  # Validation for level
        self.name = name
        self.level = level

# Sample API endpoint to create a course
@app.route('/api/v1/courses', methods=['POST'])
def create_course():
    data = request.json
    try:
        # Extract name and level from the incoming JSON data
        name = data.get('name')
        level = data.get('level')

        # Validate that both name and level are provided
        if not name or not level:
            return jsonify({"error": {"code": "E001", "message": "Both name and level are required."}}), 400

        # Create a new course instance
        new_course = Course(name=name, level=level)

        # Add the new course to the session and commit to the database
        db.session.add(new_course)
        db.session.commit()
        
        # Return success message with course details
        return jsonify({"message": "Course created successfully!", "course": {"id": new_course.id, "name": new_course.name, "level": new_course.level}}), 201

    except ValueError as e:
        # Handle validation errors
        return jsonify({"error": {"code": "E002", "message": str(e)}}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": {"code": "E003", "message": "An unexpected error occurred."}}), 500
```