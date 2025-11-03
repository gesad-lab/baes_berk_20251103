import pytest
from flask import Flask, json
from src.app import create_app  # Assuming a factory method to create your app
from src.models import db, User  # Assuming User is your model
from src.routes import register_routes  # Assuming routes are registered here

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create database tables
        yield client
        db.drop_all()  # Clean up after tests


def test_user_registration_success(client):
    """Test user registration with valid data."""
    response = client.post('/api/v1/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'securepassword'
    })

    assert response.status_code == 201
    assert response.json['message'] == 'User registered successfully'
    assert User.query.filter_by(username='testuser').count() == 1


def test_user_registration_duplicate(client):
    """Test user registration with duplicate username."""
    client.post('/api/v1/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'securepassword'
    })

    response = client.post('/api/v1/register', json={
        'username': 'testuser',
        'email': 'testuser2@example.com',
        'password': 'anotherpassword'
    })

    assert response.status_code == 400
    assert response.json['error']['code'] == 'E002'  # Assuming E002 is for duplicate username
    assert response.json['error']['message'] == 'Username already exists'


def test_user_registration_invalid_email(client):
    """Test user registration with invalid email format."""
    response = client.post('/api/v1/register', json={
        'username': 'testuser3',
        'email': 'invalidemail',  # Invalid email
        'password': 'securepassword'
    })

    assert response.status_code == 400
    assert response.json['error']['code'] == 'E001'  # Assuming E001 is for invalid email format
    assert response.json['error']['message'] == 'Invalid email format'


def test_user_data_retrieval_success(client):
    """Test successful data retrieval for a registered user."""
    client.post('/api/v1/register', json={
        'username': 'testuser4',
        'email': 'testuser4@example.com',
        'password': 'securepassword'
    })
    
    response = client.get('/api/v1/users/testuser4')

    assert response.status_code == 200
    assert response.json['username'] == 'testuser4'
    assert response.json['email'] == 'testuser4@example.com'


def test_user_data_retrieval_not_found(client):
    """Test data retrieval for a user that doesn't exist."""
    response = client.get('/api/v1/users/nonexistentuser')

    assert response.status_code == 404
    assert response.json['error']['code'] == 'E003'  # Assuming E003 is for user not found
    assert response.json['error']['message'] == 'User not found'