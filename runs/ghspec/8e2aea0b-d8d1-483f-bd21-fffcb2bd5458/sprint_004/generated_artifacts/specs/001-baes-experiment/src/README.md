# Updated README.md

# Student Registration System

## API Endpoints

### Enroll Student in Course

- **Endpoint**: `POST /students/{student_id}/enroll`
- **Description**: Enroll a student in a specific course. This associates the course with the student's record.
- **Request Body**:
    ```json
    {
      "course_id": "integer"
    }
    ```
- **Response**:
    - **Status Code**: `200 OK`
    - **Response Body**:
    ```json
    {
      "message": "Student successfully enrolled in course.",
      "student_id": "integer",
      "course_id": "integer"
    }
    ```

### View Student Courses

- **Endpoint**: `GET /students/{student_id}/courses`
- **Description**: Retrieve a list of all courses associated with a specific student. This allows tracking of the student's academic progress.
- **Response**:
    - **Status Code**: `200 OK`
    - **Response Body**:
    ```json
    [
      {
        "course_id": "integer",
        "name": "string"
      },
      // ... other courses
    ]
    ```

### Error Handling for Invalid Enrollment

- **Description**: If an administrator attempts to enroll a student in a course that does not exist, an appropriate error message will be returned.
- **Error Response**:
    - **Status Code**: `400 Bad Request`
    - **Response Body**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid course ID: The course does not exist.",
        "details": {}
      }
    }
    ```

## Database Migrations

Ensure that you have updated your database schema to reflect the new relationship between students and courses. The student entity should now contain an array of course identifiers. Use the following commands to run migrations:

```bash
flask db migrate
flask db upgrade
```

## Testing

Ensure to run tests corresponding to the new endpoints to verify their functionality. Tests should cover successful enrollments, retrieval of student course lists, and proper error handling for invalid enrollments.