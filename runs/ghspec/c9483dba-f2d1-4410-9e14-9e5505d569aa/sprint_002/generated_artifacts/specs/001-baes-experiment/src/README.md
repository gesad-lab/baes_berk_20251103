# README.md

# Student Management Web Application

Welcome to the Student Management Web Application! This application facilitates the management of student records, including their personal information.

## Features

- Create a new student with a name and email
- Retrieve student details by ID

## API Endpoints

### Create Student

`POST /students`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

**Response:**
- **201 Created**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

### Retrieve Student

`GET /students/<id>`

**Response:**
- **200 OK**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **404 Not Found** (if the student does not exist)
    ```json
    {
      "error": {
        "code": "E404",
        "message": "Student not found"
      }
    }
    ```

## Testing

To ensure our application behaves correctly, we have implemented automated tests for the following scenarios:

- **Successful retrieval of a student by ID**
- **Handling of non-existent student ID**

### Example Test Cases

```python
from flask import json
from tests import create_app, db

def test_create_student(client):
    response = client.post('/students', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'Jane Doe'
    assert response.json['email'] == 'jane.doe@example.com'

def test_get_student_success(client):
    # Assuming a student with ID 1 exists
    response = client.get('/students/1')
    assert response.status_code == 200
    assert response.json['id'] == 1

def test_get_student_not_found(client):
    response = client.get('/students/999')  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Student not found"}}
```

## Database Migration

To add the email field to the Student model, run the following commands:
```bash
flask db migrate -m "Add email field to Student model"
flask db upgrade
```

## Conclusion

This application is aimed at helping educational institutions and developers manage student data effectively. The feature of adding an email field broadens the possibilities for future functionalities related to communication and notifications.

For any issues, feel free to reach out via our support channels.

Happy coding!