import pytest
import os
import tempfile
from my_app import create_app, db

@pytest.fixture(scope='session')
def app():
    """Create a new instance of the Flask application for testing."""
    # Create a temporary database for tests
    db_fd, db_path = tempfile.mkstemp()
    os.close(db_fd)

    # Create the Flask app with test configurations
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })

    with app.app_context():
        db.create_all()  # Create tables for the tests

    yield app

    with app.app_context():
        db.drop_all()  # Clean up the database after tests are done
    os.remove(db_path)  # Remove the temporary database file

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test runner for CLI commands."""
    return app.test_cli_runner()