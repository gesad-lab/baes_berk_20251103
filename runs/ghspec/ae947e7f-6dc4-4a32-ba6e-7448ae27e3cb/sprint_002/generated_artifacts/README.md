---
# README.md

## Project Setup and Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Ensure all database migrations are up to date:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## API Usage Examples

### Creating a New Student with Email

```bash
curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{
    "name": "John Doe",
    "email": "johndoe@example.com"
}'
```

### Retrieving a Student

```bash
curl -X GET "http://localhost:8000/students/1"
```

## Explanation of the Database Schema and Model Structure

- **Students Table**:
  - `id`: Unique identifier for each student (Primary Key)
  - `name`: Name of the student
  - `email`: Unique email address of the student

---

## Integration Tests for API Email Functionalities

### Overview

Integration tests ensure the functionality of API endpoints for creating and retrieving students with associated email addresses.

### Test Cases

1. **Test Creation of a New Student with Valid Email**:
   - Ensure that a student can be created with a valid email address and that the response contains the expected fields.

2. **Test Email Validation**:
   - Ensure that attempts to create a student with an invalid email format are rejected with appropriate error messages.

3. **Test Unique Email Constraint**:
   - Ensure that attempts to create a second student with the same email address receive a conflict error.

---

### Sample Integration Tests (to be added in `tests/api/test_students.py`)

```python
def test_create_student_with_valid_email(client):
    """
    Test creating a new student with valid data including email.
    """
    response = client.post("/students", json={"name": "Jane Doe", "email": "janedoe@example.com"})
    assert response.status_code == 201  # 201 Created
    assert response.json() == {"id": 2, "name": "Jane Doe", "email": "janedoe@example.com"}

def test_create_student_with_invalid_email(client):
    """
    Test creating a new student with an invalid email format.
    """
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalid-email"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format"}}

def test_create_student_with_duplicate_email(client):
    """
    Test creating a new student with an existing email.
    """
    client.post("/students", json={"name": "John Doe", "email": "johndoe@example.com"})
    response = client.post("/students", json={"name": "Another John", "email": "johndoe@example.com"})
    assert response.status_code == 409  # 409 Conflict
    assert response.json() == {"error": {"code": "E003", "message": "Email already exists"}}
```

--- 

Make sure to implement the above tests in `tests/api/test_students.py` and run the test suite using `pytest` to ensure everything functions correctly.