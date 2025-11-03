---
# README.md

## Teacher Management API

### Overview
This API allows users to create and manage teacher entities within the application. It includes endpoints to add a new teacher, retrieve teacher details, and handle errors gracefully when required information is missing.

### API Endpoints

1. **POST /teachers**
   - This endpoint is used to create a new teacher.
   - **Request Body**:
     - `name`: string (required)
     - `email`: string (required)
   - **Response**:
     - On success (HTTP 201), returns: 
       ```json
       {"message": "Teacher added successfully."}
       ```
     - On error (HTTP 400), returns:
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name and email are required."
         }
       }
       ```

2. **GET /teachers/{id}**
   - This endpoint is used to retrieve a specific teacher by their ID.
   - **Response**:
     - On success (HTTP 200), returns teacher details:
       ```json
       {
         "id": <id>,
         "name": "<name>",
         "email": "<email>"
       }
       ```
     - On error (HTTP 404), returns:
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Teacher not found."
         }
       }
       ```

### Error Handling
In all cases where responses indicate a failure (either due to missing fields in the creation request or a request for a non-existent teacher), the API will return clear and actionable error messages with appropriate HTTP status codes.

### Testing Error Cases
To ensure the correctness of the error handling in the Teacher Management API, the following tests will be written in `tests/test_teacher.py`:

```python
import pytest

def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher added successfully."}

def test_create_teacher_without_name(client):
    response = client.post("/teachers", json={"email": "jane@example.com"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name and email are required."
        }
    }

def test_create_teacher_without_email(client):
    response = client.post("/teachers", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name and email are required."
        }
    }

def test_get_teacher(client):
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane@example.com"
    }

def test_get_non_existing_teacher(client):
    response = client.get("/teachers/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
```

### Development Workflow
1. Implement the Teacher model and new API endpoints in the respective modules.
2. Execute the database migration to create the Teacher table.
3. Perform tests to confirm that all functional requirements are met, including error case handling.
4. Update this README.md file with instructions for using the new Teacher entities.
---