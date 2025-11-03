```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Importing the FastAPI application

@pytest.fixture
def client():
    return TestClient(app)

def test_create_teacher(client):
    response = client.post('/teachers', json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Jane Doe"

def test_create_teacher_missing_fields(client):
    response = client.post('/teachers', json={"email": "jane.doe@example.com"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"  # Error code for missing fields

def test_create_teacher_invalid_email(client):
    response = client.post('/teachers', json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E002"  # Assuming E002 is for invalid email format
```