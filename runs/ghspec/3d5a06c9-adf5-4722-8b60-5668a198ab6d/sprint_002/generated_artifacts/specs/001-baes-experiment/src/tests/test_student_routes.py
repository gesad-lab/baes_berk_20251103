```python
import pytest

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_list_students(client):
    # Step 1: Create a couple of students
    client.post('/students', json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    client.post('/students', json={"name": "Bob Johnson", "email": "bob.johnson@example.com"})
    
    # Step 2: Request the list of students
    response = client.get('/students')
    
    # Step 3: Validate the response
    assert response.status_code == 200
    students = response.json()
    
    # Step 4: Check the response data for the created students
    assert len(students) == 2  # We should have two students
    assert any(student['email'] == "alice.smith@example.com" for student in students)
    assert any(student['email'] == "bob.johnson@example.com" for student in students)
    
    # Ensure the names are also included
    assert any(student['name'] == "Alice Smith" for student in students)
    assert any(student['name'] == "Bob Johnson" for student in students)
```