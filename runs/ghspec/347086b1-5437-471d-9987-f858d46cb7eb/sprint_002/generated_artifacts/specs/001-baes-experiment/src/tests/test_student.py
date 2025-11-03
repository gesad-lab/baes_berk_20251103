# tests/test_student.py

def test_create_student(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_create_student_missing_name(client):
    # Test case for creating a student without a name
    response = client.post("/students", json={})
    # Expecting a 400 Bad Request response due to missing name
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"  # Name is required

def test_create_student_with_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_missing_email(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E002"  # Email is required

def test_create_student_invalid_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "not-an-email"})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E003"  # Invalid email format