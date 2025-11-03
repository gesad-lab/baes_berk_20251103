# README.md

# API Documentation

## Overview
This document provides an overview of the API endpoints available in the application.

## Base URL
The base URL for the API is `http://localhost:5000/api/v1`.

## Endpoints

### Students

#### Create a Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Request Body**:
  - `name` (string, required): The name of the student. Must be non-empty.
  
- **Response**:
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: If the name is missing or invalid.
  
- **Example Request**:
```json
{
  "name": "John Doe"
}
```

- **Example Response**:
```json
{
  "id": 1,
  "name": "John Doe"
}
```

#### Get All Students

- **Endpoint**: `/students`
- **Method**: `GET`

- **Response**:
  - **200 OK**: Returns a list of all students.
  
- **Example Response**:
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

#### Get a Student by ID

- **Endpoint**: `/students/<id>`
- **Method**: `GET`
- **Path Parameters**:
  - `id` (integer, required): The ID of the student to retrieve.

- **Response**:
  - **200 OK**: Returns the student object.
  - **404 Not Found**: If the student with the given ID does not exist.

- **Example Response**:
```json
{
  "id": 1,
  "name": "John Doe"
}
```

#### Update a Student

- **Endpoint**: `/students/<id>`
- **Method**: `PUT`
- **Path Parameters**:
  - `id` (integer, required): The ID of the student to update.
- **Request Body**:
  - `name` (string, required): The updated name for the student.

- **Response**:
  - **200 OK**: Returns the updated student object.
  - **400 Bad Request**: If the name is invalid.
  - **404 Not Found**: If the student does not exist.

- **Example Request**:
```json
{
  "name": "Johnathan Doe"
}
```

- **Example Response**:
```json
{
  "id": 1,
  "name": "Johnathan Doe"
}
```

#### Delete a Student

- **Endpoint**: `/students/<id>`
- **Method**: `DELETE`
- **Path Parameters**:
  - `id` (integer, required): The ID of the student to delete.

- **Response**:
  - **204 No Content**: If the deletion is successful.
  - **404 Not Found**: If the student does not exist.

## Error Responses
All error responses will follow the format:
```json
{
  "error": {
    "code": "E001",
    "message": "Detailed error message."
  }
}
```

**Note**: Please ensure that all requests are made with appropriate headers specifying the content type, typically `application/json`. 

## Running the Application
To run the application, ensure all dependencies are installed and execute:

```bash
flask run
```

Make sure to set the environment variable correctly for the Flask application.