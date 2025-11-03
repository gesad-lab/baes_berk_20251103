```python
import requests

BASE_URL = "http://localhost:8000/teachers"  # Base URL for Teacher API

def test_create_teacher_with_valid_details():
    """Test creating a teacher with valid details."""
    response = requests.post(BASE_URL, json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    
    assert response.status_code == 201  # Confirm creation status
    teacher = response.json()
    assert teacher["name"] == "Jane Smith"
    assert teacher["email"] == "jane.smith@example.com"

    # Verify the teacher is listed in the returned teacher list
    teachers_response = requests.get(BASE_URL)
    assert teachers_response.status_code == 200
    teachers = teachers_response.json()
    assert any(t["id"] == teacher["id"] for t in teachers)  # Ensure created teacher is in the list


def test_create_teacher_missing_fields():
    """Test creating a teacher with missing fields raises errors."""
    missing_name_response = requests.post(BASE_URL, json={"email": "no_name@example.com"})
    assert missing_name_response.status_code == 400  # Bad Request expected
    assert "name" in missing_name_response.json()["error"]["message"]

    missing_email_response = requests.post(BASE_URL, json={"name": "No Email"})
    assert missing_email_response.status_code == 400  # Bad Request expected
    assert "email" in missing_email_response.json()["error"]["message"]

    missing_both_response = requests.post(BASE_URL, json={})
    assert missing_both_response.status_code == 400  # Bad Request expected
    assert "name" in missing_both_response.json()["error"]["message"]
    assert "email" in missing_both_response.json()["error"]["message"]


def test_fetch_all_teachers():
    """Test fetching the list of all teachers."""
    response = requests.get(BASE_URL)
    
    assert response.status_code == 200  # Ensure the request was successful
    teachers = response.json()
    assert isinstance(teachers, list)  # Ensure the response is a JSON array
    
    # Optionally check the properties of returned teachers if necessary
    for teacher in teachers:
        assert "id" in teacher
        assert "name" in teacher
        assert "email" in teacher
```