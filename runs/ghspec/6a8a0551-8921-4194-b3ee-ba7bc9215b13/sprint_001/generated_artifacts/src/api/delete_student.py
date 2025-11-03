from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError, validates

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create the database schema on startup
@app.before_first_request
def create_tables():
    db.create_all()

# Schema for student validation
class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise ValidationError('Name cannot be empty.')

# Define the DELETE endpoint for deleting a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    """Delete a student by ID.

    Args:
        id (int): The ID of the student to delete.

    Returns:
        JSON: Confirmation of deletion or error message if student not found.
    """
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": {"code": "E404", "message": "Student not found"}}), 404

    db.session.delete(student)
    db.session.commit()  # Commit the deletion to the database

    return jsonify({"message": "Student deleted successfully"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)