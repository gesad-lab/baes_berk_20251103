# Updated README.md

# Student Management System

A comprehensive system for managing students, courses, and enrollments.

## API Documentation

### Course Management API

This section outlines the endpoints available for managing courses in the system.

#### 1. Create a Course

`POST /api/courses`

**Request Body**:
```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

**Success Response**:
- **Code**: 201 Created
- **Content**:
```json
{
  "id": 1,
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

**Error Response**:
- **Code**: 400 Bad Request
- **Content**:
```json
{
  "error": {
    "code": "E001",
    "message": "Name and level are required fields.",
    "details": {}
  }
}
```

**Notes**:
- Both `name` and `level` fields are required.
- The response will include the ID of the newly created course.

#### 2. Retrieve a Course by ID

`GET /api/courses/{id}`

**Path Parameters**:
- `id` (integer): The ID of the course to retrieve.

**Success Response**:
- **Code**: 200 OK
- **Content**:
```json
{
  "id": 1,
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

**Error Response**:
- **Code**: 404 Not Found
- **Content**:
```json
{
  "error": {
    "code": "E002",
    "message": "Course not found.",
    "details": {}
  }
}
```

**Notes**:
- If the course with the specified ID does not exist, a 404 error will be returned.

### Database Migration

- Ensure to run the database migration for the newly added `courses` table that includes `id`, `name`, and `level` fields.

### Existing Data

- The update to include courses will not affect existing student data in the database.

### Development and Setup

Refer to the [development instructions](docs/development.md) for further setup instructions.

### Health Check Endpoint

A health check endpoint is available at `/api/health` to monitor the state of the service.

--- 

This update includes new API documentation for course management, detailing how to create and retrieve course records while enforcing necessary validations on the input data.