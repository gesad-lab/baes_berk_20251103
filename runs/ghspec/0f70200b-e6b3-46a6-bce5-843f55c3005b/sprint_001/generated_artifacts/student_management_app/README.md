# Student Management Application

## Overview

The Student Management Application is a simple web application designed to manage Student entities effectively. Each Student consists of a single required field, `name`, which is stored in a SQLite database for persistence. This application serves as an example of how to create, retrieve, and manage student data using an API.

## API Endpoints

### 1. Create a Student

- **Endpoint**: `POST /students`
- **Description**: Creates a new student with a required `name` field.
- **Request Body**:
  ```json
  {
      "name": "John Doe"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: If the `name` is missing. Response example:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name is required."
        }
    }
    ```

### 2. Retrieve All Students

- **Endpoint**: `GET /students`
- **Description**: Retrieves a list of all students.
- **Response**:
  - **200 OK**: Returns an array of student objects.
    ```json
    [
        {
            "id": 1,
            "name": "John Doe"
        },
        {
            "id": 2,
            "name": "Jane Smith"
        }
    ]
    ```

### 3. Retrieve a Student by ID

- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieves a specific student's details by their ID.
- **Response**:
  - **200 OK**: Returns the student object.
  - **404 Not Found**: If the student with the specified ID does not exist. Response example:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Student not found."
        }
    }
    ```

## Database Setup

The application automatically initializes the SQLite database schema upon startup. Follow the steps below to get started:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd student_management_app
   ```

2. Install the required dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Run the application:
   ```bash
   poetry run python src/app.py
   ```

The application will create the SQLite database file `students.db` if it does not already exist.

## Testing the Application

The application includes a test suite to verify the API functionality. To run the tests, use the following command:
```bash
pytest tests/
```

## Conclusion

This application provides a foundational structure for managing student data through API endpoints. For additional information on usage, refer to the API documentation.