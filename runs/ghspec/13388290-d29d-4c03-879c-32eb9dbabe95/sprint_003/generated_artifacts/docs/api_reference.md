# Updated API Documentation

## API Reference

### Courses Endpoints

This document details the newly implemented `/courses` endpoints for the API.

#### 1. Create Course

- **Endpoint**: `/api/v1/courses`
- **Method**: `POST`
- **Description**: Creates a new course.

- **Request Body**:
```json
{
    "title": "Introduction to Programming",
    "description": "An introductory course on programming concepts",
    "duration": 10,
    "teacher_id": 1
}
```
- **Expected Response**:
  - **Status Code**: 201 Created
  - **Response Body**:
```json
{
    "id": 1,
    "title": "Introduction to Programming",
    "description": "An introductory course on programming concepts",
    "duration": 10,
    "teacher_id": 1,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
}
```

#### 2. Get Course

- **Endpoint**: `/api/v1/courses/{id}`
- **Method**: `GET`
- **Description**: Retrieves a specific course by ID.

- **Path Parameters**:
  - `id`: The ID of the course to retrieve.

- **Expected Response**:
  - **Status Code**: 200 OK
  - **Response Body**:
```json
{
    "id": 1,
    "title": "Introduction to Programming",
    "description": "An introductory course on programming concepts",
    "duration": 10,
    "teacher_id": 1,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
}
```

#### 3. Update Course

- **Endpoint**: `/api/v1/courses/{id}`
- **Method**: `PUT`
- **Description**: Updates an existing course.

- **Path Parameters**:
  - `id`: The ID of the course to update.

- **Request Body**:
```json
{
    "title": "Advanced Programming",
    "description": "A course on advanced programming topics",
    "duration": 15
}
```
- **Expected Response**:
  - **Status Code**: 200 OK
  - **Response Body**:
```json
{
    "id": 1,
    "title": "Advanced Programming",
    "description": "A course on advanced programming topics",
    "duration": 15,
    "teacher_id": 1,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T01:00:00Z"
}
```

#### 4. Delete Course

- **Endpoint**: `/api/v1/courses/{id}`
- **Method**: `DELETE`
- **Description**: Deletes a specific course.

- **Path Parameters**:
  - `id`: The ID of the course to delete.

- **Expected Response**:
  - **Status Code**: 204 No Content

### Setup Instructions

To set up the project, ensure all dependencies are installed and configured. You can run the application with:

```bash
python app.py
```

### Running Tests

To execute the test suite:

```bash
pytest
```

### Examples of Using the API

To create a course, you can send a POST request to `/api/v1/courses` with the required course details in the body.

Make sure to replace `{id}` with the actual course ID in the URL when retrieving, updating, or deleting a course.

---

This documentation provides a comprehensive guide on using the new `/courses` endpoints for both developers and users.