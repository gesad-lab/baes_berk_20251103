---
# API Documentation

## Course and Teacher Management API

This API allows for the management of courses and teacher assignments. The following endpoints are available for interacting with courses and their associated teachers.

### Assign a Teacher to a Course

- **Endpoint**: `POST /courses/{courseId}/assignTeacher`
  
- **Description**: This endpoint allows the assignment of a teacher to a specific course.

- **Request Body**:
  ```json
  {
      "teacherId": 1
  }
  ```

- **Response (200 OK)**:
  ```json
  {
      "id": 1,
      "teacher_id": 1,
      "teacher": {
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```

- **Error Responses**:
  - **400 Bad Request**: If the request body is invalid (e.g., missing `teacherId`).
  - **404 Not Found**: If the specified course does not exist.

### Retrieve Course Details

- **Endpoint**: `GET /courses/{courseId}`

- **Description**: This endpoint retrieves details about a specific course, including information about the assigned teacher.

- **Response (200 OK)**:
  ```json
  {
      "id": 1,
      "title": "Course Title",
      "description": "Course Description",
      "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
      }
  }
  ```

- **Error Responses**:
  - **404 Not Found**: If the specified course does not exist.

### Update Teacher Assignment

- **Endpoint**: `PUT /courses/{courseId}/assignTeacher`
  
- **Description**: This endpoint updates the teacher assignment for a specific course.

- **Request Body**:
  ```json
  {
      "teacherId": 2
  }
  ```

- **Response (200 OK)**:
  ```json
  {
      "id": 1,
      "teacher_id": 2,
      "teacher": {
          "name": "Jane Smith",
          "email": "jane.smith@example.com"
      }
  }
  ```

- **Error Responses**:
  - **400 Bad Request**: If the request body is invalid (e.g., missing `teacherId`).
  - **404 Not Found**: If the specified course does not exist.

### Additional Notes

- Ensure to handle proper validations for the request inputs.
- All endpoint responses include appropriate status codes and error messages when applicable.

---