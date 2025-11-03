# README.md

## Student Management API Documentation

This document outlines the API endpoints available in the Student Management application, including the request and response formats, as well as error handling conventions.

### API Endpoints

The API provides the following endpoints to manage students:

#### 1. Create Student

- **Endpoint**: `POST /students`
- **Description**: Creates a new student.
- **Request Format**:
  ```json
  {
    "name": "John Doe",
    "age": 20,
    "grade": "Sophomore"
  }
  ```
- **Response Format**:
  - **Success**:
    - Status: `201 Created`
    ```json
    {
      "message": "Student created successfully.",
      "student_id": 1
    }
    ```
  - **Error**:
    - Status: `400 Bad Request`
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid input: 'name' is required."
      }
    }
    ```

#### 2. Retrieve Student

- **Endpoint**: `GET /students/<id>`
- **Description**: Retrieves a student by their ID.
- **Response Format**:
  - **Success**:
    - Status: `200 OK`
    ```json
    {
      "student": {
        "id": 1,
        "name": "John Doe",
        "age": 20,
        "grade": "Sophomore"
      }
    }
    ```
  - **Error**:
    - Status: `404 Not Found`
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

#### 3. Update Student

- **Endpoint**: `PUT /students/<id>`
- **Description**: Updates an existing student's information.
- **Request Format**:
  ```json
  {
    "name": "Johnathan Doe",
    "age": 21,
    "grade": "Junior"
  }
  ```
- **Response Format**:
  - **Success**:
    - Status: `200 OK`
    ```json
    {
      "message": "Student updated successfully."
    }
    ```
  - **Error**:
    - Status: `400 Bad Request`
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid input: 'name' is required."
      }
    }
    ```
    - Status: `404 Not Found`
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

#### 4. Delete Student

- **Endpoint**: `DELETE /students/<id>`
- **Description**: Deletes a student by their ID.
- **Response Format**:
  - **Success**:
    - Status: `204 No Content`
  - **Error**:
    - Status: `404 Not Found`
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

### Error Handling

All endpoints will return errors in the following structured JSON format:

```json
{
  "error": {
    "code": "E001",
    "message": "Error message describing the issue."
  }
}
```

Common error codes:
- **E001**: Invalid input or missing required fields.
- **E002**: Resource not found.

### Testing

To validate the functionality of the API, the following tests should be conducted:
- Confirm that creating, retrieving, updating, and deleting students works as expected.
- Validate that appropriate errors are returned for invalid inputs (e.g., missing name).
- Ensure JSON responses are correctly formatted.

### Technology Stack

- Web Framework: Flask
- ORM/Database: SQLAlchemy with SQLite
- Testing Framework: Pytest

---

This documentation serves as a comprehensive guide for interacting with the Student Management API. Follow the outlined formats closely to ensure correct functionality and error handling.