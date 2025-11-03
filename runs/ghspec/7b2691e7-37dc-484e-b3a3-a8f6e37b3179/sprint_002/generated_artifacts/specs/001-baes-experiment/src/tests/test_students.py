```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))  # New field for storing email

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    email = data.get('email')  # Capture email from the request
    
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    # Create a new Student instance
    student = Student(name=name, email=email)
    db.session.add(student)
    
    try:
        db.session.commit()
    except IntegrityError:
        return jsonify({'error': 'Student could not be created'}), 400

    # Modify response to include email in the response
    return jsonify({
        'id': student.id,
        'name': student.name,
        'email': student.email  # Include email in response
    }), 201

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create database tables
        yield client

def test_create_student_with_email(client):
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_without_email(client):
    response = client.post('/students', json={'name': 'Jane Doe'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Jane Doe'
    assert 'email' in data  # Email should still be present, potentially as 'null'
```