# New content for `docs/api_documentation.md`

# API Documentation

## Course Management

### Assign Teacher to Course

- **Endpoint**: `POST /courses/{course_id}/assign-teacher/{teacher_id}`
- **Description**: Assign a Teacher to an existing Course. 
- **Request Parameters**:
  - `course_id` (path parameter): The ID of the Course you want to assign the Teacher to.
  - `teacher_id` (path parameter): The ID of the Teacher to be assigned to the Course.
  
- **Request Body**: None required.

- **Response**:
  - **201 Created**: If the Teacher was successfully assigned to the Course.
  - **400 Bad Request**: If either `course_id` or `teacher_id` is invalid.
  - **404 Not Found**: If the specified Course or Teacher does not exist.

- **Example Request**:
    ```http
    POST /courses/1/assign-teacher/2
    ```

- **Example Response** (Success):
    ```json
    {
      "message": "Teacher successfully assigned to the course."
    }
    ```

### Retrieve Course Details

- **Endpoint**: `GET /courses/{course_id}`
- **Description**: Retrieve all details of a specific Course, including the assigned Teacher’s details.
- **Request Parameters**:
  - `course_id` (path parameter): The ID of the Course.

- **Response**:
  - **200 OK**: Returns the Course details with Teacher information if found.
  - **404 Not Found**: If the specified Course does not exist.

- **Example Request**:
    ```http
    GET /courses/1
    ```

- **Example Response** (Success):
    ```json
    {
      "course_id": 1,
      "course_name": "Introduction to Programming",
      "teacher": {
        "teacher_id": 2,
        "name": "John Doe"
      }
    }
    ```

### Notes
- All endpoints require authentication and proper authorization to ensure users have the right permissions. 
- Ensure data validation on `course_id` and `teacher_id` for all requests to prevent errors and ensure data integrity. 

# End of API Documentation Update