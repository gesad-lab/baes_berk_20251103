# README.md

# Student Management API

## Overview
This project implements a Student Management API that allows users to create, retrieve, and manage student data effectively. The API has been enhanced to include an email field for better communication and identification of students.

## Project Setup
To set up the project, ensure you have the required dependencies installed. You can do this by running:

```bash
pip install -r requirements.txt
```

## API Endpoints

### Create a Student
- **Endpoint**: `POST /students`
- **Description**: This endpoint allows for the creation of a new student.
- **Request Body**:
  ```json
  {
    "name": "string (required)",
    "email": "string (required)"
  }
  ```
- **Success Response**:
  - **Code**: 201 Created
  - **Content**:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```
  
- **Error Response**:
  - **Code**: 400 Bad Request
  - **Content**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email is required",
        "details": {}
      }
    }
    ```

### Retrieve a Student
- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieves the details of a specific student by their ID.
- **Path Parameters**:
  - `id`: The ID of the student to retrieve.
  
- **Success Response**:
  - **Code**: 200 OK
  - **Content**:
    ```json
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
    ```

## Database Schema
The database schema for the Student entity has been updated to include the following fields:
- `id`: Integer, Primary Key
- `name`: String, Required
- `email`: String, Required

## Usage Examples
To create a new student, you can use the following `curl` command:

```bash
curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
```

To retrieve a student by ID, use:

```bash
curl -X GET http://localhost:8000/students/1
```

## Summary
The addition of the email field enhances the student management experience by allowing better communication and tracking of student information. Please refer to the API documentation for detailed usage instructions and examples.