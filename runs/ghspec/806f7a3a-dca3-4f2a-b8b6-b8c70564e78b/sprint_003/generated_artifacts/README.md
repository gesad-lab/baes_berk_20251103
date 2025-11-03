# README.md

# Project Title

## Overview

This project provides an API for managing courses and students, allowing users to create, retrieve, and update records.

## Course API Endpoints

The following endpoints are available for managing courses:

### 1. Create Course
- **Endpoint**: `POST /api/v1/courses`
- **Request Body**: 
  ```json
  {
    "name": "Mathematics",
    "level": "Advanced"
  }
  ```
- **Responses**:
  - `201 Created`: Returned when the course is successfully created.
  - `400 Bad Request`: Returned if validation fails (e.g., missing name or level).

### 2. Retrieve Course by ID
- **Endpoint**: `GET /api/v1/courses/<id>`
- **Responses**:
  - `200 OK`: Returns the course details in JSON format. Example response:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Advanced"
    }
    ```
  - `404 Not Found`: Returned if the course does not exist.

### 3. Update Course
- **Endpoint**: `PUT /api/v1/courses/<id>`
- **Request Body**: 
  ```json
  {
    "name": "Mathematics",
    "level": "Intermediate"
  }
  ```
- **Responses**:
  - `200 OK`: Returned when the course is successfully updated.
  - `400 Bad Request`: Returned for validation errors (e.g., empty name or level).
  - `404 Not Found`: Returned if the course does not exist.

## Database Migration

The application includes a migration process to set up the courses table. Existing student data is preserved during this migration.

## Testing

To ensure the functionality of the Course API, unit tests will be implemented for all endpoints. These tests will verify:
- Successful creation of courses.
- Retrieval of course information by ID.
- Updating course details with validation checks.

## Setup Instructions

1. Install dependencies.
2. Set up the database.
3. Run migrations to create necessary tables.
4. Start the application and test API endpoints.

For more comprehensive API documentation, please refer to `/docs/api.md`.