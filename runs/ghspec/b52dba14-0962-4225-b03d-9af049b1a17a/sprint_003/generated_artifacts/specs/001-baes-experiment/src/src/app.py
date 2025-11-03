```python
from flask import Flask, request, jsonify, abort
from src.api.course_routes import course_routes
from src.models.course_model import Course
from src.database import db

app = Flask(__name__)

# Register the course routes with the Flask app
app.register_blueprint(course_routes, url_prefix='/courses')

if __name__ == '__main__':
    # Initialize the database and create tables if they don't exist
    with app.app_context():
        db.create_all()  # Ensure that the Course table is created

    app.run(debug=True)

# src/api/course_routes.py
from flask import Blueprint, request, jsonify, abort
from src.models.course_model import Course
from src.services.course_service import create_course, get_course, update_course

course_routes = Blueprint('course_routes', __name__)

@course_routes.route('', methods=['POST'])
def add_course():
    """Create a new course."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'level' not in data:
        abort(400, description='E001: Both name and level are required.')

    course = create_course(data['name'], data['level'])
    return jsonify(course), 201

@course_routes.route('/<int:course_id>', methods=['GET'])
def retrieve_course(course_id):
    """Retrieve a course by ID."""
    course = get_course(course_id)
    if course is None:
        abort(404, description='E002: Course not found.')
    
    return jsonify(course), 200

@course_routes.route('/<int:course_id>', methods=['PUT'])
def modify_course(course_id):
    """Update a course by ID."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'level' not in data:
        abort(400, description='E001: Both name and level are required.')

    course = update_course(course_id, data['name'], data['level'])
    if course is None:
        abort(404, description='E002: Course not found.')

    return jsonify(course), 200

# src/models/course_model.py
from src.database import db

class Course(db.Model):
    """Course model to represent the course table in the database."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

# src/services/course_service.py
from src.models.course_model import Course
from src.database import db

def create_course(name: str, level: str):
    """Create a new course and save it to the database."""
    course = Course(name=name, level=level)
    db.session.add(course)
    db.session.commit()
    return {
        'id': course.id,
        'name': course.name,
        'level': course.level,
    }

def get_course(course_id: int):
    """Retrieve a course by its ID."""
    return Course.query.get(course_id)

def update_course(course_id: int, name: str, level: str):
    """Update course details by ID."""
    course = get_course(course_id)
    if course:
        course.name = name
        course.level = level
        db.session.commit()
        return {
            'id': course.id,
            'name': course.name,
            'level': course.level,
        }
    return None
```