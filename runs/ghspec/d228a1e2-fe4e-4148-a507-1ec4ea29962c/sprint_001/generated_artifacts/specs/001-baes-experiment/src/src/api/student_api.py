from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    """Model representing a student."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.before_first_request
def create_tables():
    """Create database tables for the Student model if they do not exist."""
    db.create_all()

@app.route('/students', methods=['GET'])
def list_students():
    """List all students in the database.

    Returns a JSON array of student objects with their ID and name.
    Responds with an empty array if no students are found.
    """
    students = Student.query.all()  # Retrieve all student records
    return jsonify([{"id": student.id, "name": student.name} for student in students]), 200

if __name__ == '__main__':
    app.run(debug=True)