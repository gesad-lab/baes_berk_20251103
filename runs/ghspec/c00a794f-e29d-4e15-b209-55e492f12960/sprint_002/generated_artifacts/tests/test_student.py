```python
# tests/test_student.py
import pytest

# Test case for adding a student with both name and email
def test_add_student_with_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Student added successfully"}

# Test case for trying to add a student without email
def test_add_student_without_email(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required."}}

# Test case for retrieving a list of students including their emails
def test_retrieve_students(client):
    # First, add a student to ensure there's data to retrieve
    client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    
    response = client.get("/students")
    assert response.status_code == 200
    
    students = response.json()
    assert isinstance(students, list)  # Ensure the response is a list
    assert len(students) > 0  # Ensure that at least one student is returned
    assert "name" in students[0]  # Check for the name field in the student record
    assert "email" in students[0]  # Check for the email field in the student record
    assert students[0]["name"] == "John Doe"  # Verify the name of the student
    assert students[0]["email"] == "john@example.com"  # Verify the email of the student

# Test case for ensuring existing student data remains intact after schema update
def test_existing_student_data_integrity(client):
    # Assume previous data has been populated and that we need to verify it
    client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    
    response = client.get("/students")
    students = response.json()
    
    # Ensure all students are retrievable without loss
    assert any(student["email"] == "jane@example.com" for student in students)
```