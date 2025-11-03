# conftest.py

import pytest
from src.app import create_app  # import your Flask app factory
from src.extensions import db  # import your database instance

@pytest.fixture(scope='session')
def app():
    """Create a Flask application instance for testing."""
    app = create_app('testing')  # Use 'testing' config for tests
    with app.app_context():
        yield app

@pytest.fixture(scope='session')
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

@pytest.fixture(scope='function', autouse=True)
def reset_db():
    """Reset the database before each test to ensure a clean state."""
    db.create_all()  # Create tables
    yield  # Run test
    db.session.remove()  # Clean up the current session
    db.drop_all()  # Drop tables after each test

@pytest.fixture(scope='function')
def sample_data():
    """Insert sample data into the database for testing purposes."""
    # [Insert logic to add sample data to the database here]
    pass  # Replace with actual sample data insertion logic

# Additional fixtures can be added as needed for more complex testing scenarios