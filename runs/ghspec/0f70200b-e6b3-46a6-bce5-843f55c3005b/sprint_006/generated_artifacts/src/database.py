# Update README.md to reflect new API endpoints and database schema changes related to teacher assignments

## Updated README.md

# Student Management Application

## Overview

This application allows for the management of students, courses, and teachers, providing an API for interaction and data retrieval.

## API Endpoints

### Teachers
- **Create a Teacher**
  - `POST /teachers`
  - Request Body: `{ "name": "John Doe", "subject": "Mathematics" }`
  - Response: `201 Created`

### Courses
- **Get all Courses**
  - `GET /courses`
  - Response: `200 OK`

- **Get a Course**
  - `GET /courses/{id}`
  - Response: `200 OK` with course details including assigned teacher.

- **Update an existing Course**
  - `PATCH /courses/{id}`
  - Request Body: `{ "teacher_id": 1 }`  // assuming teacher with ID 1 exists
  - Response:
    - `200 OK` on success
    - `404 Not Found` if course does not exist.

## Database Schema Changes

### Courses Table
- **Updated Fields**:
  - `id`: integer (Primary Key)
  - `name`: string
  - `description`: string
  - `teacher_id`: integer (Foreign Key to Teachers.id, allows null values)

## Migration

A database migration has been created to incorporate the `teacher_id` field in the Courses table while preserving data for existing entities. Ensure to run the migration before using the new API features.

## Responses

All API responses are in JSON format that indicates success or failure in the actions of assigning teachers to courses and fetching course details.

## User Scenarios & Testing

1. **Assigning a Teacher to a Course**:
   - As an admin user, PATCH request to `/courses/{id}` will allow assigning a teacher to existing courses.
   - Verify successful assignment and response.

2. **Fetching Course with Teacher Information**:
   - As an admin user, view course details including associated teacher information via `GET /courses/{id}`.

## Additional Notes

- Ensure to check the Swagger/OpenAPI documentation for further details on the API and endpoint specifications.
- Please raise any issues or bugs encountered while using the API via our GitHub issue tracker.