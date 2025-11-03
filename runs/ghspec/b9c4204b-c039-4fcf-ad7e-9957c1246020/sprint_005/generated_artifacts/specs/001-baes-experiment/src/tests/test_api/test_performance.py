```markdown
# API Specifications

## Enroll Student in Course
- **Endpoint**: `POST /enroll`
- **Request Body**:
  ```json
  {
      "student_id": 1,
      "course_id": 2
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "status": "enrolled",
        "student_id": 1,
        "course_id": 2
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course ID is required"
        }
    }
    ```

## Create Teacher
- **Endpoint**: `POST /teachers`
- **Request Body**:
  ```json
  {
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "status": "created",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Name is required"
        }
    }
    ```

## Retrieve Teachers
- **Endpoint**: `GET /teachers`
- **Response**:
  - **Success (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }
    ]
    ```
  - **Error (500 Internal Server Error)**:
    ```json
    {
        "error": {
            "code": "E003",
            "message": "Unable to retrieve teachers"
        }
    }
    ```

### Usage Instructions
1. **POST /teachers**:
   - To create a new teacher, send a `POST` request to `/teachers` with a JSON body containing the teacher's `name` and `email`.
   - Ensure that the `name` is provided; otherwise, an error will be returned.

2. **GET /teachers**:
   - To retrieve a list of all teachers, send a `GET` request to `/teachers`.
   - This will return a JSON array of teachers with their `id`, `name`, and `email`.
```