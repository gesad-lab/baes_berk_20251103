# README.md

# Course Management API

## Overview
This API allows for the management of courses, including the ability to create, list, and update courses in our educational platform. The API is built using Flask and structured to follow RESTful principles.

## Functional Requirements

### 1. Create a Course
- **Method**: `POST`
- **Endpoint**: `/courses`
- **Request Body**:
  - `name`: string (required)
  - `level`: string (required)
- **Response**:
  - **201 Created** with JSON confirmation of the created course including `name` and `level`.

#### Example Request
```http
POST /courses
Content-Type: application/json

{
    "name": "Introduction to Python",
    "level": "Beginner"
}
```

#### Example Response
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "name": "Introduction to Python",
    "level": "Beginner"
}
```

### 2. List All Courses
- **Method**: `GET`
- **Endpoint**: `/courses`
- **Response**:
  - **200 OK** with a JSON array of course records, each including `name` and `level`.

#### Example Request
```http
GET /courses
```

#### Example Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

[
    {
        "name": "Introduction to Python",
        "level": "Beginner"
    },
    {
        "name": "Advanced Python",
        "level": "Advanced"
    }
]
```

### 3. Update a Course
- **Method**: `PUT`
- **Endpoint**: `/courses/{id}`
- **Request Body**:
  - `name`: string (optional)
  - `level`: string (optional)
- **Response**:
  - **200 OK** with JSON confirmation including any updated fields.

#### Example Request
```http
PUT /courses/1
Content-Type: application/json

{
    "level": "Intermediate"
}
```

#### Example Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "name": "Introduction to Python",
    "level": "Intermediate"
}
```

## Database Schema
The database includes a new table for the Course entity with the following structure:
- `id`: Integer (auto-incremented primary key)
- `name`: String (required)
- `level`: String (required)

**Note**: Ensure that the database migration preserves all existing Student data.

## Development Steps
1. **Setup Project Environment**:
    - Ensure the virtual environment is configured with the same dependencies.
    - Update `requirements.txt` as needed.

2. **Modify Database Schema**:
    - Create a migration script using Alembic to add a new `courses` table without affecting existing data.
    - The migration script will handle creating `courses` with columns `id`, `name`, and `level`.

3. **Update API Module**:
    - Create new route handlers for creating, retrieving, and updating courses in the API.
    - Ensure that the HTTP responses are formatted according to the API contracts.

4. **Implement Input Validation Logic**:
    - Validate that `name` and `level` are provided when creating or updating a course.
    - Implement error handling to return structured error messages for invalid inputs.

5. **Ensure Error Handling**:
    - Adjust the global error handler to manage course validation errors and return appropriate HTTP codes and messages.

6. **Testing**:
    - Create test cases to verify all functionalities related to course management.
    - Ensure coverage targets meet our established standards (70% general, 90% in critical paths).

7. **Documentation**:
    - Update this README to include details about the new Course entity and document the API operations.