# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new `Course` entity within the existing system to manage courses effectively. This new entity will allow the application to store relevant information about various courses, which can be linked to students in the future. The addition of the `Course` entity complements the existing `Student` entity and enhances the overall capability of the Student Management Web Application.

## User Scenarios & Testing
1. **Create a New Course**:
   - As an administrator, I want to create a new course by providing a name and level so that I can maintain an accurate record of all available courses.
   - Test: Validate that a POST request to the API successfully creates a course with a valid name and level.

2. **Retrieve Courses**:
   - As a user, I want to retrieve a list of all courses so that I can view available options.
   - Test: Validate that a GET request returns a list of courses in JSON format, including both the name and level fields.

3. **Course Name and Level Validation**:
   - As a user, I want to receive an error message if I attempt to create a course without providing a name or level.
   - Test: Validate that the application returns a clear error message when attempting to create a course with missing required fields.

## Functional Requirements
1. The application must provide an updated API endpoint to create a new course:
   - **Endpoint**: `/courses` (POST)
   - **Request Body**:
     ```json
     {
         "name": "<string>",
         "level": "<string>"
     }
     ```
   - **Response**:
     - Status code 201 (Created) with the created course object, including both name and level attributes.

2. The application must provide an updated API endpoint to retrieve all courses:
   - **Endpoint**: `/courses` (GET)
   - **Response**:
     - Status code 200 (OK) with a JSON array of course objects, including their name and level.

3. The application must validate the input data:
   - The `name` field must be a non-empty string.
   - The `level` field must be a non-empty string. The application must return a status code 400 (Bad Request) if the validation fails for either field, along with an error message.

4. The SQLite database schema must be updated to include the new `Course` table:
   - **Table Name**: `courses`
   - **Fields**:
     - `id`: Integer (auto-increment, primary key)
     - `name`: String (required, cannot be null)
     - `level`: String (required, cannot be null)

5. A database migration must be created to add the `Course` table while preserving existing `Student` data.

## Success Criteria
1. Users can create a new course entry with both a name and a level, receiving a 201 status code along with the course data in the response.
2. Users can retrieve all course entries, and the response includes a valid JSON array of course objects, displaying their names and levels.
3. Input validation works correctly, returning a 400 status code with a descriptive error message when invalid input (missing name or level) is provided.
4. The application starts without errors, and the SQLite database is correctly updated with the new schema for the `Course` entity while maintaining the integrity of existing `Student` data.

## Key Entities
- **Course**:
  - Attributes:
    - `id`: Integer (auto-increment, primary key)
    - `name`: String (required, cannot be null)
    - `level`: String (required, cannot be null)

## Assumptions
- The web application will continue to operate in an environment that supports Python 3.11+.
- SQLite remains a feasible choice for this application, due to its lightweight nature and capability to handle migrations effectively.

## Out of Scope
- User interface changes are not included; this feature focuses on back-end API functionality only.
- Advanced business logic around course management or associations with students will not be addressed in this iteration.
- Real-time notifications or updates related to course changes or registrations are not included in this scope.