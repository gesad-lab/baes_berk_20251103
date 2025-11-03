# API Documentation

## Overview

This API is built using FastAPI, providing a fast and efficient interface for managing student records. It utilizes SQLite as a lightweight database solution, with SQLAlchemy as the ORM for seamless database operations. The API is fully documented and can be explored using Swagger UI.

## Base URL

The base URL for accessing the API endpoints is:
```
http://localhost:8000
```

## Endpoints

Below you'll find a list of available endpoints along with their usage.

### 1. Create a Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Description**: Creates a new student record.
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "age": 20,
        "email": "john.doe@example.com"
    }
    ```
- **Response**:
    - **201 Created**: Returns the created student object.
    - **400 Bad Request**: If the input data is invalid.

### 2. Retrieve All Students

- **Endpoint**: `/students`
- **Method**: `GET`
- **Description**: Retrieves a list of all student records.
- **Response**:
    - **200 OK**: Returns an array of student objects.

### 3. Retrieve a Student by ID

- **Endpoint**: `/students/{student_id}`
- **Method**: `GET`
- **Description**: Retrieves a student record by its unique ID.
- **Path Parameters**:
    - `student_id`: The ID of the student to retrieve.
- **Response**:
    - **200 OK**: Returns the student object if found.
    - **404 Not Found**: If the student with the given ID does not exist.

### 4. Update a Student

- **Endpoint**: `/students/{student_id}`
- **Method**: `PUT`
- **Description**: Updates an existing student record.
- **Path Parameters**:
    - `student_id`: The ID of the student to update.
- **Request Body**:
    ```json
    {
        "name": "John Smith",
        "age": 21,
        "email": "john.smith@example.com"
    }
    ```
- **Response**:
    - **200 OK**: Returns the updated student object.
    - **404 Not Found**: If the student with the given ID does not exist.
    - **400 Bad Request**: If the input data is invalid.

### 5. Delete a Student

- **Endpoint**: `/students/{student_id}`
- **Method**: `DELETE`
- **Description**: Deletes a student record by its unique ID.
- **Path Parameters**:
    - `student_id`: The ID of the student to delete.
- **Response**:
    - **204 No Content**: If the deletion is successful.
    - **404 Not Found**: If the student with the given ID does not exist.

## API Documentation Access

For interactive API documentation, you can access the Swagger UI at:
```
http://localhost:8000/docs
```

This interface allows you to view and test all API endpoints directly.