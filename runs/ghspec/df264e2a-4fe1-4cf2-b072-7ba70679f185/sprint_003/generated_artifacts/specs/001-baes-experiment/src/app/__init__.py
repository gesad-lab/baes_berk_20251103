# README.md

# Project Title

## Overview

This project is an application that allows users to manage students and courses, enabling easy creation and retrieval of student and course data.

## Course Feature

### User Scenarios & Testing

1. **Create a Course**
   - **Scenario**: A user submits a new Course record with a valid name and level.
   - **Expected Outcome**: The course is created, and a success message with the course details is returned in JSON format.

2. **Retrieve a Course**
   - **Scenario**: A user requests the details of an existing Course that includes the name and level fields.
   - **Expected Outcome**: The application returns the Course's details in JSON format.

3. **Error Handling for Missing Fields**
   - **Scenario**: A user submits a new Course record without providing either name or level.
   - **Expected Outcome**: An error message is returned indicating that both fields are required.

4. **Database Migration**
   - **Scenario**: The application starts up after the addition of the Course entity.
   - **Expected Outcome**: The database schema is updated to include the Course table without impacting existing Student data.

## API Endpoints

### Create a Course
- **Endpoint**: `POST /courses`
- **Request**:
  - Body (JSON):
    ```json
    {
      "name": "Course Name",
      "level": "Course Level"
    }
    ```
- **Responses**:
  - **201 Created**: Returns the created course details.
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "level": "Course Level"
    }
    ```
  - **400 Bad Request**: Returns an error if either field is missing.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Both name and level are required."
      }
    }
    ```

### Retrieve a Course
- **Endpoint**: `GET /courses/{id}`
- **Responses**:
  - **200 OK**: Returns the Course details.
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "level": "Course Level"
    }
    ```
  - **404 Not Found**: Returns an error if the Course does not exist.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found."
      }
    }
    ```

## Database Migration
- Upon application startup, the application will execute a migration to add a `Course` table without losing any pre-existing Student records. 

## Conclusion

This new feature enhances the application's capabilities, allowing users to manage course records effectively and seamlessly integrate with existing student functionality.