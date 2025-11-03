import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_client():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    with TestClient(app) as client:
        yield client
        
    # Cleanup: drop the database tables after tests
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    # Create a new database session for each test
    connection = engine.connect()
    transaction = connection.begin()
    db = TestingSessionLocal()
    
    # Override the dependency to use the test database session
    app.dependency_overrides[get_db] = lambda: db
    
    yield db  # Provide the test database session to the test
    
    db.close()
    transaction.rollback()
    connection.close()


def test_create_student(db_session, test_client):
    """Test creating a new student record."""
    response = test_client.post(
        "/api/students/",
        json={"name": "John Doe", "age": 20, "grade": "A"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_get_student(db_session, test_client):
    """Test fetching a student record."""
    response = test_client.get("/api/students/1/")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


def test_update_student(db_session, test_client):
    """Test updating an existing student record."""
    response = test_client.put(
        "/api/students/1/",
        json={"name": "John Doe", "age": 21, "grade": "A+"}
    )
    assert response.status_code == 200
    assert response.json()["age"] == 21


def test_delete_student(db_session, test_client):
    """Test deleting a student record."""
    response = test_client.delete("/api/students/1/")
    assert response.status_code == 204  # No Content


def test_get_non_existing_student(db_session, test_client):
    """Test fetching a non-existing student record."""
    response = test_client.get("/api/students/999/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_create_student_with_invalid_data(db_session, test_client):
    """Test creating a student record with invalid data."""
    response = test_client.post(
        "/api/students/",
        json={"name": "", "age": 20}  # Missing the 'grade'
    )
    assert response.status_code == 400
    assert "detail" in response.json()  # Validate error response content