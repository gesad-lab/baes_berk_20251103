import requests

BASE_URL = "http://localhost:8000/students"

def test_create_student_with_email():
    """Test creating a new student with valid name and email."""
    response = requests.post(BASE_URL, json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_retrieve_all_students_with_email():
    """Test retrieving all student records, ensuring email is included."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)
    assert all("email" in student for student in students)

def test_update_student_email():
    """Test updating a student's email."""
    student_id = 1  # Assuming this ID exists for the test
    new_email = "john.new@example.com"
    response = requests.put(f"{BASE_URL}/{student_id}", json={"email": new_email})
    assert response.status_code == 200
    updated_student = response.json()
    assert updated_student["email"] == new_email

def test_create_student_with_invalid_email():
    """Test creating a student with an invalid email format."""
    response = requests.post(BASE_URL, json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 400
    error_response = response.json()
    assert error_response["error"]["code"] == "E001"  # Assuming E001 is the code for invalid email


def test_update_student_with_invalid_email():
    """Test updating a student's email with an invalid format."""
    student_id = 1  # Assuming this ID exists for the test
    response = requests.put(f"{BASE_URL}/{student_id}", json={"email": "invalid-email"})
    assert response.status_code == 400
    error_response = response.json()
    assert error_response["error"]["code"] == "E001"  # Same as above, adjust as necessary

# Run tests
if __name__ == "__main__":
    test_create_student_with_email()
    test_retrieve_all_students_with_email()
    test_update_student_email()
    test_create_student_with_invalid_email()
    test_update_student_with_invalid_email()