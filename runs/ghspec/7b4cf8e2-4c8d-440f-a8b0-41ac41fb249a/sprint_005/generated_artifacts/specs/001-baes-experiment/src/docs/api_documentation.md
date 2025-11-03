# Complete file content for docs/api_documentation.md

# API Documentation

## Overview

This document provides information about the RESTful API endpoints available for managing teachers within the application.

## Base URL

All API endpoints are prefixed with `/api/v1`.

## Endpoints

### Create Teacher

- **URL**: `/teachers`
- **Method**: `POST`
- **Description**: Creates a new teacher using the data provided in the request body.
- **Request Body**:
    ```json
    {
        "name": "string",
        "subject": "string",
        "email": "string"
    }
    ```
- **Response**:
    - **201 Created**: 
        ```json
        {
            "id": "integer",
            "name": "string",
            "subject": "string",
            "email": "string"
        }
        ```
    - **400 Bad Request**: 
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Invalid input data"
            }
        }
        ```

### Get Teacher

- **URL**: `/teachers/<int:teacher_id>`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific teacher by their ID.
- **URL Parameters**:
    - `teacher_id`: The ID of the teacher to retrieve
- **Response**:
    - **200 OK**: 
        ```json
        {
            "id": "integer",
            "name": "string",
            "subject": "string",
            "email": "string"
        }
        ```
    - **404 Not Found**: 
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Teacher not found"
            }
        }
        ```

### List Teachers

- **URL**: `/teachers`
- **Method**: `GET`
- **Description**: Lists all teachers in the system.
- **Response**:
    - **200 OK**: 
        ```json
        [
            {
                "id": "integer",
                "name": "string",
                "subject": "string",
                "email": "string"
            },
            ...
        ]
        ```

## Error Handling

All error responses follow a consistent format:
```json
{
    "error": {
        "code": "Exxx",
        "message": "Error message describing what went wrong"
    }
}
``` 

## Conclusion

This API allows for the management of teacher objects, with the ability to create, retrieve, and list teachers. Ensure to follow the correct format for requests and handle responses appropriately in your application.