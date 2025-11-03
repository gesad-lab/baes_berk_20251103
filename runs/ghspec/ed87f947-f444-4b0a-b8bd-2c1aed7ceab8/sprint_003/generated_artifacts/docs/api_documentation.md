---
# API Documentation

## Course Management API

### Overview
This API allows for the management of course entities, including creating, retrieving, and updating course information. Each course has an ID, a name, and a level.

### Endpoints

#### 1. Create Course
- **POST** `/api/v1/courses`
- **Request**:
  - **Content-Type**: application/json
  - **Body**:
  ```json
  {
      "name": "Data Science 101",
      "level": "Beginner"
  }
  ```
- **Response** (201 Created):
  - **Body**:
  ```json
  {
      "id": 1,
      "name": "Data Science 101",
      "level": "Beginner"
  }
  ```
- **Description**: Creates a new course with the specified name and level.

#### 2. Retrieve Course
- **GET** `/api/v1/courses/{id}`
- **Response** (200 OK):
  - **Body**:
  ```json
  {
      "id": 1,
      "name": "Data Science 101",
      "level": "Beginner"
  }
  ```
- **Description**: Retrieves details of a specific course by its ID.

#### 3. Update Course
- **PUT** `/api/v1/courses/{id}`
- **Request**:
  - **Content-Type**: application/json
  - **Body**:
  ```json
  {
      "name": "Advanced Data Science",
      "level": "Intermediate"
  }
  ```
- **Response** (200 OK):
  - **Body**:
  ```json
  {
      "id": 1,
      "name": "Advanced Data Science",
      "level": "Intermediate"
  }
  ```
- **Description**: Updates the details of an existing course.

### Error Responses
- **400 Bad Request**: Returned when input validation fails or required fields are missing.
- **404 Not Found**: Returned when a course with the specified ID does not exist.

### Changelog
- Added API endpoints for Course management including creation, retrieval, and updating of course entities.
- Ensure all API responses adhere to the specified formats.

### Notes
- All endpoints must include appropriate authentication and authorization checks to ensure secure access to course data.
- Error handling should provide meaningful error messages in response formats.

---