```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.models import Course  # Assuming a Course model is created in models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'  # Update as necessary
db = SQLAlchemy(app)

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course."""
    data = request.get_json()
    
    # Validate the request body
    if 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and level are required."}}), 400

    course = Course(name=data['name'], level=data['level'])
    
    db.session.add(course)
    db.session.commit()
    
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Retrieve course details by ID."""
    course = Course.query.get(course_id)
    
    if course is None:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404
    
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
```