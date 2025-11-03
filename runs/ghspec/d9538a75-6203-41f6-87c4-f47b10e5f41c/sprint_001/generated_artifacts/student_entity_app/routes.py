```python
from flask import Blueprint, request, jsonify
from .database import init_db
from .models import Student
from flask_sqlalchemy import SQLAlchemy

# Initialize a new Blueprint for the student routes
student_bp = Blueprint('student', __name__)

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        init_db()  # Ensure the database and tables are created on startup

    app.register_blueprint(student_bp, url_prefix='/api')
    return app

@student_bp.route('/students', methods=['POST'])
def create_student():
    """
    Create a new student record.
    
    The request must contain a JSON body with the following fields:
    - name: A required string representing the student's name.

    Returns:
        - HTTP 201 if the student is created successfully.
        - HTTP 400 if the input validation fails.
    """
    data = request.get_json()
    name = data.get('name')

    if not name or not isinstance(name, str):
        return jsonify({"error": {"code": "E001", "message": "Invalid name format, name is required and must be a string."}}), 400

    # Create a new student record
    new_student = Student(name=name)
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"id": new_student.id, "name": new_student.name}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": {"code": "E002", "message": f"Error creating student: {str(e)}"}}), 500

@student_bp.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all student records.

    Returns:
        - HTTP 200 with a JSON array of student objects.
    """
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

# Ensure this function is called when the application starts
def init_db():
    """Initialize the database schema for the application."""
    db.create_all()
```