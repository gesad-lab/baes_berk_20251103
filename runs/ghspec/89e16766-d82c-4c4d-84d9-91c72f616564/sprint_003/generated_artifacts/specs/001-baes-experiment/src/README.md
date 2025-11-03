# README.md

# Project Title

This project is focused on creating and managing courses, with a robust API for handling course records.

## API Endpoints

### 1. Create Course Endpoint

- **Endpoint**: `/courses`
- **Method**: `POST`
- **Request**: 
    - JSON body containing:
      - `name` (string, required): The name of the course.
      - `level` (string, required): The level of the course.
- **Response**: 
    - On success: 
      ```json
      {
        "message": "Course created successfully.",
        "course_id": "<generated_course_id>"
      }
      ```
    - On error (missing fields):
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Course name is required."
        }
      }
      ```
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Course level is required."
        }
      }
      ```

### 2. Retrieve Course Endpoint

- **Endpoint**: `/courses/<id_or_name>`
- **Method**: `GET`
- **Response**:
    - On success: 
      ```json
      {
        "id": "<course_id>",
        "name": "<course_name>",
        "level": "<course_level>"
      }
      ```
    - On error (course not found):
      ```json
      {
        "error": {
          "code": "E003",
          "message": "Course not found."
        }
      }
      ```

## Database Schema

A new Course table must be created in the database schema with the following required fields:

- **name**: A string representing the course name.
- **level**: A string representing the course level.

## Database Migration

A migration must be executed to add the Course table to the database without affecting the existing Student data.

## Error Handling

- Proper error responses must be provided for validation failures, such as missing fields. Ensure that the application checks for the presence of required fields (`name` and `level`) and returns structured error messages as specified.

## Success Criteria

- 100% of valid course records can be created successfully with both name and level fields.
- 100% of existing and new course records can be retrieved accurately using both name and ID.
- The application should display appropriate error messages for missing required fields.
- The database schema should be updated without errors, with the new Course table added.

## Testing

Automated tests will be implemented to validate the scenarios above, ensuring that:

- Course records with valid inputs can be successfully created and retrieved.
- Proper error messages are displayed for missing name and level fields.

## New Test Cases

- Test the successful creation of a course with valid name and level.
- Test retrieval of a course by both ID and name.
- Test that error messages are returned for missing name and level.