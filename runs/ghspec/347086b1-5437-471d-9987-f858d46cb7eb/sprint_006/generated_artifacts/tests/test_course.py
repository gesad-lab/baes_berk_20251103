```python
# tests/test_course.py

def test_assign_teacher_to_course(client):
    """Test assigning a teacher to a course successfully."""
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200  # Check for success response
    assert response.json() == {"message": "Teacher assigned successfully."}  # Check the success message

def test_assign_teacher_without_id(client):
    """Test assigning a teacher without providing an ID fails validation."""
    response = client.post("/courses/1/assign_teacher", json={})
    assert response.status_code == 400  # Expect a bad request status code
    assert response.json()["error"]["code"] == "E002"  # Validation error for missing teacher_id

def test_get_course_with_teacher(client):
    """Test retrieving a course details including associated teacher."""
    response = client.get("/courses/1")
    assert response.status_code == 200  # Ensure successful retrieval
    assert "teacher" in response.json()  # Ensure teacher details are included in the response
```