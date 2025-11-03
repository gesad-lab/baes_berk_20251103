```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is initialized in `main.py`
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models import Student

# Initialize the test client
client = TestClient(app)

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override to use the test database
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the tables after tests are done
    Base.metadata.drop_all(bind=engine)


def test_create_student(setup_database):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_retrieve_student_valid(setup_database):
    client.post("/students", json={"name": "Jane Doe"})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Doe"}

def test_retrieve_student_not_found(setup_database):
    response = client.get("/students/99")  # Assuming 99 does not exist
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Student not found."
        }
    }
```