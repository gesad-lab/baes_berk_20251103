import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from http import HTTPStatus

# Setup Flask and SQLAlchemy for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create the database schema
with app.app_context():
    db.create_all()

# Define the route to retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student is None:
        # Return a 404 error if the student is not found.
        return jsonify({"error": {"code": "E404", "message": "Student not found."}}), HTTPStatus.NOT_FOUND
    return jsonify({"id": student.id, "name": student.name}), HTTPStatus.OK

# Define the test class for Student model
class TestStudent:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        """Setup the database for each test."""
        db.drop_all()
        db.create_all()

    def test_student_retrieval_non_existing(self):
        """Test retrieval of a non-existing student (should return an error)."""
        # Attempt to retrieve a student that doesn't exist
        response = app.test_client().get('/students/999')  # Assuming 999 is a non-existing ID
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json == {"error": {"code": "E404", "message": "Student not found."}}