# docs/api_reference.md

# API Reference

## Courses

### Create Course

**POST** `/api/v1/courses`

Create a new course.

**Request Body**:
```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

**Response**:
- **201 Created**: Course successfully created.
    ```json
    {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    ```

- **400 Bad Request**: Missing required fields.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name field is required."
        }
    }
    ```

### Retrieve Course

**GET** `/api/v1/courses/{course_id}`

Retrieve a course by its ID.

**Path Parameters**:
- `course_id` (integer): The ID of the course to retrieve.

**Response**:
- **200 OK**: Course found.
    ```json
    {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
    }
    ```

- **404 Not Found**: Course does not exist.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

### Summary

This documentation reflects the updated API endpoints for handling course creation and retrieval. Ensure to use the `/api/v1/courses` endpoint with the proper request structure as outlined above for creating a new course and retrieving existing courses by their IDs. Make sure HTTP status codes and error messages are handled correctly for a smooth integration experience.