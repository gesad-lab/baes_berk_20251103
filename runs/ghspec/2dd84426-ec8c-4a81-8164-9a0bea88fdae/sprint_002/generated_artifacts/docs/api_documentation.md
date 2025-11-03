# docs/api_documentation.md

# API Documentation

## Overview

This document outlines the API endpoints available for our application. The API is built using Flask and follows RESTful principles. It exposes endpoints for managing student records in an SQLite database.

## Base URL

The base URL for all API requests is:

```
http://localhost:5000/api/v1
```

## Endpoints

### 1. Get All Students

- **Endpoint**: `/students`
- **Method**: `GET`
- **Description**: Retrieve a list of all students.
- **Response**:
  - **Status Code**: 200 OK
  - **Content**: A JSON array of student objects.
  
#### Example Request:
```http
GET /api/v1/students HTTP/1.1
Host: localhost:5000
```

#### Example Response:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "age": 20,
        "grade": "Sophomore"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 22,
        "grade": "Senior"
    }
]
```

### 2. Create a New Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Description**: Create a new student record.
- **Request Body**:
  - **Content**: A JSON object with the student details.
    - `name` (string): The student's name (required).
    - `age` (integer): The student's age (required).
    - `grade` (string): The student's grade (optional).
- **Response**:
  - **Status Code**: 201 Created
  - **Content**: The created student object.

#### Example Request:
```http
POST /api/v1/students HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "name": "Alice Johnson",
    "age": 21,
    "grade": "Junior"
}
```

#### Example Response:
```json
{
    "id": 3,
    "name": "Alice Johnson",
    "age": 21,
    "grade": "Junior"
}
```

### 3. Retrieve a Student by ID

- **Endpoint**: `/students/{id}`
- **Method**: `GET`
- **Description**: Retrieve a single student by their ID.
- **Response**:
  - **Status Code**: 200 OK
  - **Content**: A JSON object with the student's details.
  
#### Example Request:
```http
GET /api/v1/students/1 HTTP/1.1
Host: localhost:5000
```

#### Example Response:
```json
{
    "id": 1,
    "name": "John Doe",
    "age": 20,
    "grade": "Sophomore"
}
```

### 4. Update a Student

- **Endpoint**: `/students/{id}`
- **Method**: `PUT`
- **Description**: Update an existing student record.
- **Request Body**:
  - **Content**: A JSON object with the updated student details.
  
#### Example Request:
```http
PUT /api/v1/students/1 HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "name": "Johnathan Doe",
    "age": 21,
    "grade": "Junior"
}
```

#### Example Response:
```json
{
    "id": 1,
    "name": "Johnathan Doe",
    "age": 21,
    "grade": "Junior"
}
```

### 5. Delete a Student

- **Endpoint**: `/students/{id}`
- **Method**: `DELETE`
- **Description**: Delete a student record.
- **Response**:
  - **Status Code**: 204 No Content

#### Example Request:
```http
DELETE /api/v1/students/1 HTTP/1.1
Host: localhost:5000
```

## Error Handling

All errors will be returned in the following structured format:

```json
{
    "error": {
        "code": "E001",
        "message": "Error description",
        "details": {}
    }
}
```

## Testing

API endpoints are tested using pytest. The test suite includes various scenarios, such as retrieving, creating, updating, and deleting students.

## Conclusion

This API documentation provides a comprehensive overview of the endpoints and their functionalities. For further assistance, please refer to the source code or contact the development team.