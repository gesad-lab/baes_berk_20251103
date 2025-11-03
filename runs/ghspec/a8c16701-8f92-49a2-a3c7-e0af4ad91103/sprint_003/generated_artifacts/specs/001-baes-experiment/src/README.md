# README.md

# Project Title

## API Documentation

### Overview

This API enables users to manage courses and students in the system. The main functionalities include creating courses, retrieving course information, and ensuring all student records remain unchanged.

### Course Endpoints

#### Create Course

- **Endpoint**: `/courses/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "Course Name",
        "level": "Beginner"
    }
    ```
  - `name`: String, required. The name of the course.
  - `level`: String, required. The level of the course (e.g., Beginner, Intermediate, Advanced).

- **Response**: 
  - **Status**: `201 Created`
  - **Body**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Beginner"
    }
    ```

#### Retrieve Course

- **Endpoint**: `/courses/{course_id}`
- **Method**: `GET`
- **Response**:
  - **Status**: `200 OK`
  - **Body**:
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Beginner"
    }
    ```

- **Path Parameters**:
  - `course_id`: Integer, required. The ID of the course to retrieve.

#### Error Handling

- If the request to create a course is invalid (e.g., missing `name` or `level`), the following response is returned:
  - **Status**: `400 Bad Request`
  - **Body**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid request: 'name' and 'level' are required fields.",
            "details": {}
        }
    }
    ```

### Existing Student Records

All existing student records remain unchanged and accessible after implementing the new Course feature.

### Conclusion

This updated documentation reflects the newly implemented Course entity, ensuring clarity on the API's capabilities.