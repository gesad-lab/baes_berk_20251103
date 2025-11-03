```python
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
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name is required.",
            "details": {}
        }
    }

def test_create_student_empty_name(client):
    # Test case for creating a student with an empty name
    response = client.post("/students", json={"name": ""})
    # Expecting a 400 Bad Request response due to empty name
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Name cannot be empty.",
            "details": {}
        }
    }

def test_create_student_name_too_long(client):
    # Test case for creating a student with a name that is too long
    long_name = "A" * 256  # Assuming max length is 255
    response = client.post("/students", json={"name": long_name})
    # Expecting a 400 Bad Request response due to name being too long
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Name exceeds maximum length of 255 characters.",
            "details": {}
        }
    }
```