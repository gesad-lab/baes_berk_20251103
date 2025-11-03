# File: docs/api_documentation.md

## API Documentation

### Overview
This document outlines the API endpoints related to student entities, including the addition of the email field. 

### Base URL
```
http://localhost:5000/students
```

### Endpoints

#### Create Student

- **POST /students**
- **Description**: Create a new student record.
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
  - **name** (string, required): The name of the student.
  - **email** (string, required): The email address of the student. Must follow valid email format.

- **Response**:
  - **201 Created**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **400 Bad Request**
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format",
        "details": {}
      }
    }
    ```

#### Update Student

- **PUT /students/{id}**
- **Description**: Update an existing student record by ID.
- **Request Body**:
  ```json
  {
    "name": "John Doe Updated",
    "email": "john.doe.updated@example.com"
  }
  ```
  - **name** (string, optional): The updated name of the student.
  - **email** (string, optional): The updated email address of the student. Must follow valid email format.

- **Response**:
  - **200 OK**
    ```json
    {
      "id": 1,
      "name": "John Doe Updated",
      "email": "john.doe.updated@example.com"
    }
    ```
  - **400 Bad Request**
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format",
        "details": {}
      }
    }
    ```
  - **404 Not Found**
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found",
        "details": {}
      }
    }
    ```

#### Get Student

- **GET /students/{id}**
- **Description**: Retrieve a student record by ID.
- **Response**:
  - **200 OK**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **404 Not Found**
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found",
        "details": {}
      }
    }
    ```

### Error Codes
- **E001**: Invalid email format.
- **E002**: Student not found.

### Notes
- All responses are returned in valid JSON format, including new email information.
- Ensure that proper validation is applied to the email format to improve user input handling.