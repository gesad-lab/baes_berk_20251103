# README.md

# Project Title
Student Management Web Application

## Description
This is a web application to manage student records. Users can create, retrieve, and manage student information.

## Features
- Create a Student by providing their name.
- Retrieve a list of all Students.

## API Endpoints
### Create a Student
- **URL**: `/students`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
      "name": "string"  // The name of the student (required)
  }
  ```
- **Responses**:
  - **201 Created**: Successfully created student.
    ```json
    {
        "id": "integer",
        "name": "string"
    }
    ```
  - **400 Bad Request**: Name field is required.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "The name field is required."
        }
    }
    ```

### Retrieve Students
- **URL**: `/students`
- **Method**: `GET`
- **Responses**:
  - **200 OK**: List of all students.
    ```json
    [
        {
            "id": "integer",
            "name": "string"
        }
    ]
    ```

## Setup
1. Clone the repository.
2. Install the required dependencies.
3. Set up the SQLite database.
4. Run the application.

## Testing
To run the tests, use the following command:
```
pytest
```

## Test Cases
### Creating a Student
- Test success response with valid name.
- Test error response when name is not provided.

### Retrieving Students
- Test that all students can be fetched successfully.

### Error on Invalid Student Creation
- Test that creating a student without a name returns a validation error.

## Future Enhancements
- Add a feature for updating and deleting student records.
- Implement user authentication.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# TEST FILE: tests/test_app.py

import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema
            yield client
        db.drop_all()  # Clean up the database after tests

def test_create_student_without_name(client):
    """Test that creating a student without a name returns a validation error."""
    
    # Making a POST request to create a student without a name
    response = client.post('/students', json={"name": ""})
    
    # Assert the response status code for bad request
    assert response.status_code == 400
    
    # Assert the error response is as expected
    assert response.get_json() == {
        "error": {
            "code": "E001",
            "message": "The name field is required."
        }
    }

# Additional tests can be added here...