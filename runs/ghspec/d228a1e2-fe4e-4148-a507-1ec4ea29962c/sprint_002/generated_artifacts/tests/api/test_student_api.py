```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)  # Added email field

# Create Student API Endpoint
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    # Validate input
    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and email fields are required"}}), 400

    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"id": new_student.id, "name": new_student.name, "email": new_student.email}), 201

# Test for the Student API
@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create database tables
        yield client

def test_create_student_with_valid_data(client):
    """Test student creation with valid data."""
    response = client.post('/students', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "John Doe"
    assert data['email'] == "john.doe@example.com"

def test_create_student_without_name(client):
    """Test student creation without a name field."""
    response = client.post('/students', json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    error = response.get_json()
    assert error['error']['code'] == "E001"
    assert error['error']['message'] == "Name and email fields are required"

def test_create_student_without_email(client):
    """Test student creation without an email field."""
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 400
    error = response.get_json()
    assert error['error']['code'] == "E001"
    assert error['error']['message'] == "Name and email fields are required"

def test_create_student_with_invalid_email_format(client):
    """Test student creation with invalid email format (additional validation can be implemented)."""
    response = client.post('/students', json={"name": "John Doe", "email": "invalid_email"})
    # An additional validation for email format would ideally go here, 
    # but as per the current setup, this is not being validated yet.
    assert response.status_code == 201  # This is a placeholder for actual validation handling.

```