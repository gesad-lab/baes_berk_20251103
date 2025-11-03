# README.md

# Project Title

## Overview

This project provides an API for managing student records with functionalities such as creating, retrieving, updating, and deleting student information.

## API Documentation

### Base URL
The base URL for accessing the API is:  
```
http://<your-domain>/api/v1
```

### Endpoints

#### 1. Create Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
      "name": "string",
      "age": "integer",
      "grade": "string"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student record.
  - **400 Bad Request**: If the input data is invalid.
  
#### 2. Get Students

- **Endpoint**: `/students`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns a list of student records.
  
#### 3. Get Student by ID

- **Endpoint**: `/students/{id}`
- **Method**: `GET`
- **Response**:
  - **200 OK**: Returns the student record with the specified ID.
  - **404 Not Found**: If the student with the given ID does not exist.

#### 4. Update Student

- **Endpoint**: `/students/{id}`
- **Method**: `PUT`
- **Request Body**: 
  ```json
  {
      "name": "string",
      "age": "integer",
      "grade": "string"
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated student record.
  - **400 Bad Request**: If the input data is invalid.
  - **404 Not Found**: If the student with the given ID does not exist.

#### 5. Delete Student

- **Endpoint**: `/students/{id}`
- **Method**: `DELETE`
- **Response**:
  - **204 No Content**: Successfully deleted the student record.
  - **404 Not Found**: If the student with the given ID does not exist.

## Running the API

To run the API locally, use the following command:

```bash
uvicorn src.api:app --reload
```

## Tests

To run the tests, use:

```bash
pytest tests/
```

Make sure that the database is properly set up before running the tests. You can use the provided fixtures to ensure the tests run smoothly.