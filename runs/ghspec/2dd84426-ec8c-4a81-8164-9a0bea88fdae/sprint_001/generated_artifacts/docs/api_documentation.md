# API Documentation using Swagger/OpenAPI

# Title: Student Management API

## Overview
The Student Management API is designed to allow users to create and manage `Student` entities. Each `Student` has a mandatory `name` field, which must be provided during creation. The API supports a RESTful architecture and guarantees appropriate responses in JSON format.

## Base URL
```
http://localhost:5000
```

## Endpoints

### 1. Create a Student

- **Endpoint**: `/students`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "string"
    }
    ```

    | Field  | Type   | Required | Description               |
    |--------|--------|----------|---------------------------|
    | name   | string | Yes      | The name of the student.  |

- **Responses**:
    - **201 Created**: 
        ```json
        {
            "id": "integer",
            "name": "string"
        }
        ```
        - Description: Returns the created student object.
  
    - **400 Bad Request**: 
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Name field is required."
            }
        }
        ```
        - Description: Returned when the name field is missing.

---

### 2. Retrieve All Students

- **Endpoint**: `/students`
- **Method**: `GET`
- **Responses**:
    - **200 OK**:
        ```json
        [
            {
                "id": "integer",
                "name": "string"
            }
        ]
        ```
        - Description: Returns a JSON array of all student objects.

---

## Database Initialization
- On application startup, the database schema is automatically created, ensuring that a table for `Students` exists with a column for `name`.

## Error Handling
- All API responses include standard HTTP status codes to indicate success or failure of requests. Each error response provides an error code and message for clarity.

---

## Usage Scenarios
1. **Creating a Student**: A user can send a `POST` request to `/students` with a valid name to create a student.
2. **Failing to Create a Student**: If a `POST` request is sent to `/students` without the name field, an error response will indicate that the name is required.
3. **Retrieving Students**: Users can retrieve all students by making a `GET` request to `/students`.

---

## Conclusion
The Student Management API provides an efficient way to manage student records via its RESTful endpoints, ensuring that the user experience is smooth and intuitive.