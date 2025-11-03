```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    level = db.Column(db.String(50), nullable=False)

# API endpoint to create a course
@app.route('/api/v1/courses', methods=['POST'])
def create_course():
    """
    Create a new course with the provided name and level.
    Required fields: name, level.
    Returns JSON response with course details or error message.
    """
    
    data = request.json
    
    # Validate input fields
    if not data.get('name'):
        return jsonify({"error": {"code": "E001", "message": "Course name is required."}}), 400
    if not data.get('level'):
        return jsonify({"error": {"code": "E002", "message": "Course level is required."}}), 400

    # Create the course object
    new_course = Course(
        name=data['name'],
        level=data['level']
    )
    
    # Add the course to the database
    db.session.add(new_course)
    db.session.commit()

    # Return the newly created course details
    return jsonify({
        "id": new_course.id,
        "name": new_course.name,
        "level": new_course.level
    }), 201

# Other code, e.g., endpoint to retrieve all courses...
```