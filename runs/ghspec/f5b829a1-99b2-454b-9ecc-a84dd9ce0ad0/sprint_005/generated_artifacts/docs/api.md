---
# File: docs/api.md

## API Documentation

### Teachers API

#### Create Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
```json
{
  "name": "string",
  "email": "string"
}
```
- **Response**:
  - **201 Created**: 
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```

#### Error Handling
- **400 Bad Request**: If the name is missing.
  - **Response**:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name is required."
    }
  }
  ```
  
- **400 Bad Request**: If the email is missing.
  - **Response**:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Email is required."
    }
  }
  ```

- **400 Bad Request**: If the email format is invalid.
  - **Response**:
  ```json
  {
    "error": {
      "code": "E003",
      "message": "Invalid email format."
    }
  }
  ```

---

## Testing Scenarios

- **Test creating a teacher with valid name and email information.**
  - Ensure that a valid request returns a 201 status code and the correct response format.

- **Test attempting to create a teacher without a name to verify error handling.**
  - Verify that a request without a name returns a 400 status code with the appropriate error message.

- **Test attempting to create a teacher without an email to verify error handling.**
  - Verify that a request without an email returns a 400 status code with the appropriate error message.

- **Test attempting to create a teacher with an invalid email format to verify error handling.**
  - Verify that a request with an invalid email returns a 400 status code with the appropriate error message.

- **Ensure that the creation of teachers does not interfere with existing Student and Course data.**
  - Validate that the teacher creation process does not affect the existing Student and Course tables in any way.

---

## Example Tests

```python
def test_create_teacher_success(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_teacher_missing_email(client):
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required."}}

def test_create_teacher_invalid_email_format(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Invalid email format."}}
```
