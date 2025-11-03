# student_management/README.md

# Student Management API

This is a simple API for managing student records using FastAPI and SQLite. It allows you to create and retrieve student records.

## Table of Contents
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Examples](#examples)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   When using the API, ensure to set up any necessary environment variables as needed. An example `.env` file is provided.

## API Documentation

### Endpoints

#### Create a New Student

- **URL**: `/students`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
      "message": "Student created successfully",
      "student": {
        "name": "John Doe"
      }
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name is required"
      }
    }
    ```

#### Retrieve All Students

- **URL**: `/students`
- **Method**: `GET`
- **Response**:
  - **Success (200 OK)**:
    ```json
    [
      "John Doe",
      "Jane Smith"
    ]
    ```
  - **Error (500 Internal Server Error)**: 
    (This indicates something went wrong on the server.)

## Examples

### Example: Creating a New Student
```bash
curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"name": "John Doe"}'
```

### Example: Retrieving All Students
```bash
curl -X GET "http://localhost:8000/students"
```

## Notes

- All API responses are in JSON format.
- Ensure that the SQLite database is set up automatically upon startup of the application.

Feel free to reach out for any questions or contributions!