# Updated API Documentation

## API Reference

### Base URL
```
http://<your_host>/api
```

### Endpoints

#### Students

- **POST /students**
    - Create a new student record.
    - **Request Body**:
        ```json
        {
            "name": "string",  // Required
            "email": "string"   // Required, must be a valid email format
        }
        ```
    - **Response**:
        - **201 Created**: Returns the created student.
        ```json
        {
            "id": "integer",
            "name": "string",
            "email": "string"
        }
        ```
        - **400 Bad Request**: If the input validation fails.

- **GET /students**
    - Retrieve a list of all students.
    - **Response**:
        - **200 OK**: Returns a list of students.
        ```json
        [
            {
                "id": "integer",
                "name": "string",
                "email": "string"
            }
        ]
        ```

#### Courses

- **POST /courses**
    - Create a new course record.
    - **Request Body**:
        ```json
        {
            "name": "string",  // Required
            "level": "string"  // Required
        }
        ```
    - **Response**:
        - **201 Created**: Returns the created course.
        ```json
        {
            "id": "integer",
            "name": "string",
            "level": "string"
        }
        ```
        - **400 Bad Request**: If the input validation fails.

- **GET /courses**
    - Retrieve a list of all courses.
    - **Response**:
        - **200 OK**: Returns a list of courses.
        ```json
        [
            {
                "id": "integer",
                "name": "string",
                "level": "string"
            }
        ]
        ```

### Error Responses

Responses with errors will include an error object with a code and message:

- **400 Bad Request**
  ```json
  {
      "error": {
          "code": "E001",
          "message": "Invalid input data",
          "details": {
              "name": "This field is required",
              "level": "This field is required"
          }
      }
  }
  ```

### Implementation Notes
- Use OpenAPI for comprehensive API documentation including definitions and request/response schemas.
- All endpoints require authentication, which should be implemented in future iterations.
- Check your input data types when creating students or courses for validation.

---

This documentation reflects the current implementation and is intended for both front-end developers and API consumers, detailing how to create and retrieve students and courses while ensuring proper validation and error handling.