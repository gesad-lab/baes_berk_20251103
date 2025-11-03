```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Assuming the app and db have been initialized in your main application code
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Existing Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)

# New Course model for managing course data
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)  # Course name
    level = db.Column(db.String(50), nullable=False)  # Course level (e.g., Beginner, Intermediate)

    def to_dict(self):
        """Convert Course instance to dictionary for JSON responses."""
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level
        }

# Endpoint to create a course
@app.route('/api/v1/courses', methods=['POST'])
def create_course():
    """Create a new course with the provided data."""
    data = request.json
    if not data or 'name' not in data or 'level' not in data:
        abort(400, description='Invalid input: "name" and "level" fields are required')  # Return error if missing required fields

    new_course = Course(name=data['name'], level=data['level'])
    db.session.add(new_course)
    db.session.commit()

    return jsonify(new_course.to_dict()), 201  # Return created course data with a 201 status


# Endpoint to retrieve all courses
@app.route('/api/v1/courses', methods=['GET'])
def get_courses():
    """Retrieve all courses."""
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses]), 200  # Return all courses in JSON format
```