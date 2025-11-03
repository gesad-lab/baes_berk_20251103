import pytest
from app import create_app, db
from models.teacher import Teacher

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()  # Create the database and tables
        yield app.test_client()
        db.drop_all()  # Clean up after tests

def test_create_teacher(client):
    # Test creating a teacher with valid data
    response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["name"] == "John Doe"
    assert response.json["email"] == "john.doe@example.com"

def test_create_teacher_without_name(client):
    # Test trying to create a teacher without the name
    response = client.post('/teachers', json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Name and email are required."

def test_create_teacher_without_email(client):
    # Test trying to create a teacher without the email
    response = client.post('/teachers', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Name and email are required."

def test_create_teacher_with_empty_fields(client):
    # Test trying to create a teacher with empty fields
    response = client.post('/teachers', json={"name": "", "email": ""})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E001"
    assert response.json['error']['message'] == "Name and email are required."