import pytest
from flask import Flask
from your_application import create_app

@pytest.fixture
def app():
    """Create and configure a new Flask application instance for testing."""
    app = create_app({'TESTING': True})
    
    # Additional configuration or setup can go here if needed
    yield app

@pytest.fixture
def client(app):
    """Provide a test client for the app."""
    return app.test_client()

@pytest.fixture
def init_database():
    """Initialize the database before each test."""
    # Logic to create the database schema goes here
    # e.g., db.create_all() or similar
    pass

@pytest.fixture(autouse=True)
def run_around_tests(init_database):
    """Run database initialization automatically around each test."""
    # Any setup before tests can go here
    yield
    # Any teardown after tests can go here
    # e.g., db.drop_all() or similar if needed
