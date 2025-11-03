# README.md

# Student Management Application

This application allows users to manage Student entities via a RESTful API. Users can create and retrieve Students, ensuring proper error handling for invalid inputs and non-existent records.

## API Endpoints

### Create Student
- **URL**: `/students`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "string"  // Required: Name of the Student
  }
  ```

- **Success Response**:
  - **Code**: 201 Created
  - **Content**:
    ```json
    {
      "id": "string",        // ID of the created Student
      "name": "string",      // Name of the created Student
      "message": "Student created successfully."
    }
    ```

- **Error Response**:
  - **Code**: 400 Bad Request
  - **Content**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name field is required."
      }
    }
    ```

### Retrieve Student
- **URL**: `/students/{id}`
- **Method**: `GET`

- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "id": "string",        // ID of the requested Student
      "name": "string"       // Name of the requested Student
    }
    ```

- **Error Response**:
  - **Code**: 404 Not Found
  - **Content**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

## User Scenarios & Testing

1. **Creating a Student**:
   - **Scenario**: A user sends a request to create a new Student with a valid name.
   - **Expected Result**: The application stores the Student in the database and responds with the created Student object, including an ID and a status message.

2. **Retrieving a Student**:
   - **Scenario**: A user sends a request to retrieve a Student by ID.
   - **Expected Result**: The application returns the requested Student object as a JSON response.

3. **Creating a Student with Missing Name**:
   - **Scenario**: A user attempts to create a Student without a name.
   - **Expected Result**: The application responds with a validation error indicating that the name field is required.

4. **Retrieving a Non-existent Student**:
   - **Scenario**: A user attempts to retrieve a Student that does not exist.
   - **Expected Result**: The application returns a 404 status code with a message indicating that the Student was not found.

## Testing Implementation

### Unit Tests

#### Test Cases for Retrieving a Non-existent Student
```python
import unittest
from app import app

class TestStudentAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_retrieve_non_existent_student(self):
        # Attempt to retrieve a Student with a non-existent ID
        response = self.app.get('/students/9999')  # Assuming 9999 does not exist
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {
            "error": {
                "code": "E002",
                "message": "Student not found."
            }
        })
    
    # Additional test cases should be added here...

if __name__ == '__main__':
    unittest.main()
```

## Success Criteria
1. At least 90% of API requests (create/retrieve) return expected responses successfully in accordance with the defined API contracts.
2. The application should correctly create and retrieve Student records as per functional requirements.
3. Proper error handling for invalid inputs and non-existent records should be implemented, returning appropriate status codes and messages.

## Overview & Purpose
The purpose of this feature is to develop a simple web application that allows users to manage Student entities. Each Student will have a required name field. This application serves as an interface to create and retrieve students via a RESTful API, returning JSON responses for easy consumption by frontend applications or other services.