```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from student_app.db.database import Base, get_db

# Define a test database URL here (use appropriate configuration for testing)
TEST_DATABASE_URL = "sqlite:///./test_database.db"

@pytest.fixture(scope='module')
def test_db():
    # Setup the database engine and session
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(bind=engine)  # Create all tables in the database
    
    # Create a configured "Session" class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Dependency override
    def override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Use dependency injection to provide the test DB session
    return override_get_db()

def test_create_student(test_db):
    # Add logic here to test the creation of a student
    pass

def test_retrieve_student(test_db):
    # Add logic here to test retrieving a student by ID
    pass

def test_update_student(test_db):
    # Add logic here to test updating a student's name
    pass

def test_delete_student(test_db):
    # Add logic here to test deleting a student
    pass

```