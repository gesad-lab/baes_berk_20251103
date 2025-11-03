import pytest

@pytest.fixture
def app():
    """Create and configure a new Flask application instance for testing."""
    from src.app import create_app  # Assuming create_app function initializes Flask
    app = create_app()
    
    # Additional configurations for testing can be set here
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Use in-memory database for tests
    })
    
    with app.app_context():
        yield app  # This will be the Flask app for testing

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Initialize the database before tests."""
    from src.database import db  # Assuming db is your SQLAlchemy instance
    with app.app_context():
        db.create_all()  # Create the tables
        
        # Optionally, add sample data or perform migrations here
        
        yield  # This allows tests to run
        
        db.drop_all()  # Clean up after tests run

# You can add more fixtures as needed to setup common test scenarios.