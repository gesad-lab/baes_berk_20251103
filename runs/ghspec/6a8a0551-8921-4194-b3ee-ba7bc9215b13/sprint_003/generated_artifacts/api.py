```python
# api.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Defining the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

# Marshmallow schema for Course validation
class CourseSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    level = fields.String(required=True, validate=validate.Length(min=1))

# Create the schema instance
course_schema = CourseSchema()

@app.route('/courses/', methods=['POST'])
def create_course():
    """Create a new course with provided name and level."""
    json_data = request.get_json()
    
    # Validate input data
    try:
        validated_data = course_schema.load(json_data)
    except ValidationError as err:
        # Respond with validation errors if inputs are invalid
        return jsonify({"error": {"code": "E001", "message": "Invalid input data", "details": err.messages}}), 400

    # Create and save a new Course instance
    course = Course(**validated_data)
    db.session.add(course)
    db.session.commit()

    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

@app.route('/courses/', methods=['GET'])
def get_courses():
    """Retrieve all courses."""
    courses = Course.query.all()
    
    result = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    return jsonify(result), 200

@app.route('/courses/<int:id>/', methods=['GET'])
def get_course(id):
    """Retrieve a specific course by ID."""
    course = Course.query.get(id)
    
    if not course:
        return jsonify({"error": {"code": "E404", "message": "Course not found."}}), 404

    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200

# Initialize the database (ensure this is done in production setup)
@app.before_first_request
def create_tables():
    db.create_all()
```