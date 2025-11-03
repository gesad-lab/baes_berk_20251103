```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.models import Teacher  # Import Teacher model

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher in the database."""
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validate input data
    if not name or not email:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and email are required.'}}), 400

    # Check for email uniqueness
    if Teacher.query.filter_by(email=email).first():
        return jsonify({'error': {'code': 'E002', 'message': 'Email address already in use.'}}), 400

    # Create a new teacher
    new_teacher = Teacher(name=name, email=email)
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({'id': new_teacher.id, 'name': new_teacher.name, 'email': new_teacher.email}), 201

@app.route('/teachers', methods=['GET'])
def list_teachers():
    """Retrieve the list of teachers."""
    teachers = Teacher.query.all()
    return jsonify([{'id': teacher.id, 'name': teacher.name, 'email': teacher.email} for teacher in teachers]), 200

@app.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve details of a specific teacher by ID."""
    teacher = Teacher.query.get(teacher_id)
    
    if not teacher:
        return jsonify({'error': {'code': 'E003', 'message': 'Teacher not found.'}}), 404
    
    return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 200

@app.errorhandler(Exception)
def handle_exception(error):
    """Handle unexpected exceptions."""
    # Log the error here if needed (using your logging framework)
    return jsonify({'error': {'code': 'E500', 'message': 'An unexpected error occurred.'}}), 500
```