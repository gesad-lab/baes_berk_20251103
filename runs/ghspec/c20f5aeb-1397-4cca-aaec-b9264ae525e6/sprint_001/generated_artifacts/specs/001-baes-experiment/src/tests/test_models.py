```python
import pytest
from src.database import get_db, init_db
from src.app import create_app
from src.models import Student
from sqlalchemy import inspect

@pytest.fixture
def app():
    """Create a new Flask application instance for testing."""
    app = create_app({"TESTING": True})
    with app.app_context():
        init_db()  # Initialize the database with the schema
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the application."""
    return app.test_client()

def test_database_schema_created(app):
    """Test that the SQLite database schema is created correctly."""
    with app.app_context():
        # Check that the students table exists in the database
        inspector = inspect(get_db())
        assert 'students' in inspector.get_table_names(), "The 'students' table should exist in the database."

        # Additionally, verify that the 'name' column is present in the students table
        columns = [column['name'] for column in inspector.get_columns('students')]
        assert 'name' in columns, "The 'name' column should exist in the 'students' table."
```