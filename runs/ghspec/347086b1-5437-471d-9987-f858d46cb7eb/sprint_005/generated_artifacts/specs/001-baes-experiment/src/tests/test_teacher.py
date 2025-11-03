```python
# tests/test_teacher.py

def test_create_teacher(client):
    """Test successful creation of a Teacher."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check for success response
    assert response.json()["name"] == "John Doe"  # Check if the name matches
    assert response.json()["email"] == "john.doe@example.com"  # Check if the email matches

def test_create_teacher_with_missing_fields(client):
    """Test creation request with missing name field."""
    response = client.post("/teachers", json={"name": "", "email": "noemail@example.com"})
    assert response.status_code == 400  # Check for validation error response
    assert response.json()["error"]["code"] == "E001"  # Validation error for required fields
    
    response = client.post("/teachers", json={"name": "John Doe", "email": ""})
    assert response.status_code == 400  # Check for validation error response
    assert response.json()["error"]["code"] == "E001"  # Validation error for required fields

def test_get_teacher(client):
    """Test retrieval of a Teacher's information."""
    # Assuming a Teacher with id=1 exists in the database
    response = client.get("/teachers/1")
    assert response.status_code == 200  # Check for success response 
    assert response.json()["id"] == 1  # Verify retrieved Teacher ID
```
