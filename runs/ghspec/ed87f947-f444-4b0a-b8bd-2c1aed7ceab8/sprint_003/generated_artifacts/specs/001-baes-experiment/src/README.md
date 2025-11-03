# README.md

# Project Title

## Overview
This project is designed to manage courses, allowing users to create, retrieve, and update course information through a RESTful API. The system includes comprehensive error handling and validation to ensure that all inputs are correct.

## Migration and API Changes

### Database Migration
As part of the recent updates, a migration script has been added to create a new `courses` table in the database. This new table includes the following attributes:

- `id`: an auto-incrementing primary key.
- `name`: a required string representing the name of the course.
- `level`: a required string indicating the course level.

The SQL for creating the `courses` table is as follows:
```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level TEXT NOT NULL
);
```

This migration has been designed to ensure that it does not affect any existing student data or other entities in the database. After running the migration, you can retrieve all existing courses to verify that the `courses` table has been created successfully without impacting other data.

### API Endpoints
The following API endpoints are now available for managing courses:

1. **Create a Course**
   - **Endpoint**: `POST /courses`
   - **Request Body**:
     ```json
     {
       "name": "Introduction to Programming",
       "level": "Beginner"
     }
     ```
   - **Success Response**:
     - **Status Code**: 201 Created
     - **Response Body**:
     ```json
     {
       "id": 1,
       "name": "Introduction to Programming",
       "level": "Beginner"
     }
     ```

2. **Retrieve a Course**
   - **Endpoint**: `GET /courses/{id}`
   - **Success Response**:
     - **Status Code**: 200 OK
     - **Response Body**:
     ```json
     {
       "id": 1,
       "name": "Introduction to Programming",
       "level": "Beginner"
     }
     ```

3. **Update a Course**
   - **Endpoint**: `PUT /courses/{id}`
   - **Request Body**:
     ```json
     {
       "name": "Advanced Programming",
       "level": "Intermediate"
     }
     ```
   - **Success Response**:
     - **Status Code**: 200 OK
     - **Response Body**:
     ```json
     {
       "id": 1,
       "name": "Advanced Programming",
       "level": "Intermediate"
     }
     ```

### Error Handling
The API includes robust error handling:

- If the `name` or `level` fields are missing in requests, the API will respond with a 400 Bad Request status code and an appropriate error message.
- Example error response:
```json
{
  "error": {
    "code": "E001",
    "message": "Missing required fields: name and level",
    "details": {}
  }
}
```

## Testing
Comprehensive tests have been written to ensure that the new Course functionalities work as expected. The tests cover normal creation, retrieval, and updating of courses, as well as incorrect input scenarios. The goal is to maintain at least 70% test coverage for these new features.

## Conclusion
With these updates, the course management functionalities are now more robust and ready for use. Please make sure to run the migrations and test the new API endpoints as per the specifications outlined above.