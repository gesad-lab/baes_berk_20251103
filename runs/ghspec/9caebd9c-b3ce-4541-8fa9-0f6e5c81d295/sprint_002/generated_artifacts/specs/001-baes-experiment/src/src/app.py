```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from api.models import Student  # Import the Student model
from api.validators import validate_student_name  # Import the name validator

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/students', methods=['POST'])
def add_student():
    """Add a new student with name and email.

    Request JSON should contain:
    - name (str): The name of the student
    - email (str): The email of the student

    Returns:
    - JSON response with the created student ID and confirmation message
    - 400 Bad Request if validation fails
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validate student name
    if not validate_student_name(name):
        abort(400, description="Invalid student name.")

    # Check for email presence
    if not email:
        abort(400, description="Email is required.")

    # Create new student instance
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added", "id": new_student.id}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a student's details by their ID.

    Returns:
    - JSON response with the student's name and email
    - 404 Not Found if the student doesn't exist
    """
    student = Student.query.get_or_404(student_id)
    return jsonify({"name": student.name, "email": student.email})

if __name__ == "__main__":
    app.run(debug=True)
```