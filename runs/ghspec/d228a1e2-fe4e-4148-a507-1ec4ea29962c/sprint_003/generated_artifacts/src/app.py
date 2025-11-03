```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from your_model_file import Course  # Import the Course model
from app import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/courses', methods=['POST'])
def create_course():
    """Create a new course."""
    data = request.get_json()

    # Validate request data
    if not data or 'name' not in data or 'level' not in data:
        return jsonify({"error": {"code": "E001", "message": "Name and level are required fields."}}), 400
    
    try:
        new_course = Course(name=data['name'], level=data['level'])
        db.session.add(new_course)
        db.session.commit()
        return jsonify({"id": new_course.id, "name": new_course.name, "level": new_course.level}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": "Course already exists."}}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Database error occurred.", "details": str(e)}}), 500

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    """Retrieve a course by its ID."""
    course = Course.query.get(id)
    if not course:
        return jsonify({"error": {"code": "E004", "message": "Course not found."}}), 404
    
    return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200

@app.route('/courses', methods=['GET'])
def list_courses():
    """List all courses."""
    courses = Course.query.all()
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in courses]), 200

if __name__ == '__main__':
    app.run(debug=True)
```