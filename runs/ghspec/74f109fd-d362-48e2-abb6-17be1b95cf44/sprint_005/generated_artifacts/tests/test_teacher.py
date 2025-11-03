```python
import pytest
from src.models.teacher import Teacher
from src.repositories.teacher_repository import TeacherRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.db.migrations import run_migrations, rollback_migrations

# Setting up a test database engine
TEST_DATABASE_URL = "sqlite:///:memory:"  # In-memory database for testing
engine = create_engine(TEST_DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='module')
def test_db():
    """Set up the database for testing and roll back after tests."""
    # Create a new session for the tests
    session = Session()
    # Run migrations to create the necessary tables
    run_migrations(engine)  # Create the Teacher table
    yield session  # Provide the fixture value
    # Rollbacks after tests
    rollback_migrations(engine)  # Ensure the migrations are reversible

@pytest.fixture
def teacher_repository(test_db):
    """Fixture for initializing the TeacherRepository for tests."""
    return TeacherRepository(test_db)

def test_create_teacher_success(teacher_repository):
    """Test creating a teacher with valid data."""
    teacher_data = {"name": "John Doe", "email": "john@example.com"}
    teacher = teacher_repository.create_teacher(teacher_data['name'], teacher_data['email'])
    assert teacher.name == teacher_data['name']
    assert teacher.email == teacher_data['email']

def test_create_teacher_invalid_email(teacher_repository):
    """Test creating a teacher with invalid email."""
    with pytest.raises(IntegrityError):
        teacher_repository.create_teacher("Jane Doe", "invalid-email")

def test_create_teacher_missing_name(teacher_repository):
    """Test creating a teacher with missing name."""
    with pytest.raises(IntegrityError):
        teacher_repository.create_teacher("", "jane@example.com")

def test_retrieve_teacher_success(teacher_repository):
    """Test retrieving a teacher by ID."""
    # First create a teacher to retrieve later
    teacher = teacher_repository.create_teacher("Alice Smith", "alice@example.com")
    retrieved_teacher = teacher_repository.get_teacher_by_id(teacher.id)
    assert retrieved_teacher is not None
    assert retrieved_teacher.id == teacher.id
    assert retrieved_teacher.name == teacher.name

def test_retrieve_teacher_not_found(teacher_repository):
    """Test retrieving a teacher with a non-existent ID."""
    retrieved_teacher = teacher_repository.get_teacher_by_id(9999)  # ID that does not exist
    assert retrieved_teacher is None
```