from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize a new Flask Blueprint for students
students_bp = Blueprint('students', __name__)

# Initialize the SQLAlchemy database object
db = SQLAlchemy()

# Define the Student model
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self):
        """Convert Student object to dictionary for JSON response."""
        return {"id": self.id, "name": self.name}

# Create the database schema if it does not exist
def create_database():
    with app.app_context():
        db.create_all()

# Initialize the database
create_database()

@students_bp.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve the list of all students in the database.

    Returns:
        JSON response containing a list of students.
    """
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200

@students_bp.route('/students', methods=['POST'])
def add_student():
    """
    Add a new student.

    Request JSON Body:
        {
            "name": "Student Name"
        }
    
    Returns:
        JSON response containing the created student object or an error message.
    """
    data = request.get_json()
    
    if not data or 'name' not in data or not data['name']:
        # Return error if name is missing or empty
        return jsonify({"error": {"code": "E001", "message": "Name cannot be empty"}}), 400
    
    new_student = Student(name=data['name'])
    
    try:
        # Add the new student to the database
        db.session.add(new_student)
        db.session.commit()  # Commit the session to save changes
    except IntegrityError:
        db.session.rollback()  # Rollback in case of an integrity error
        return jsonify({"error": {"code": "E002", "message": "Student already exists."}}), 400

    return jsonify(new_student.to_dict()), 201