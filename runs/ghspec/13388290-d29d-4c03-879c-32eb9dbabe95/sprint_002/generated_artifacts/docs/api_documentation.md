# File: docs/api_documentation.md

# API Documentation

## Overview
This document outlines the API endpoints for managing Student records, detailing the expected inputs and outputs, including a new `email` field for each student.

## Endpoints

### POST /students
Create a new student record.

#### Request Body
The request body must be a JSON object with the following fields:

- **name** (string, required): The name of the student.
- **email** (string, required): The email address of the student.

#### Example Request
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### Responses
- **201 Created**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **400 Bad Request** (if `email` is missing):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Email is required"
    }
  }
  ```

### GET /students/{id}
Retrieve a student record by ID.

#### Path Parameters
- **id** (integer, required): The unique identifier of the student.

#### Responses
- **200 OK**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **404 Not Found** (if the student does not exist):
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student not found"
    }
  }
  ```

## Database Schema
The `students` table includes the following columns:

- **id**: INTEGER PRIMARY KEY AUTOINCREMENT
- **name**: TEXT NOT NULL
- **email**: TEXT NOT NULL

## Conclusion
This update adds functionality to create and retrieve student records with an email field, ensuring meaningful error handling for required fields. Please refer to the documentation above when utilizing the API.