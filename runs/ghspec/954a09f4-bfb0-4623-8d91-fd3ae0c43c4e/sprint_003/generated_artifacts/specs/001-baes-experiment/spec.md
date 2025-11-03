# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new Course entity within the existing system to support the management and categorization of courses offered. By adding this entity, we aim to enhance the system's educational capabilities, allowing for better organization and access to course information. This change builds upon the existing student data management established in the previous sprints.

## User Scenarios & Testing
1. **Creating a Course**:
   - **Scenario**: A user sends a request to create a new Course with a valid name and level.
   - **Test**: Verify that a course is successfully created, returning the correct name and level in the response.

2. **Creating a Course with Missing Fields**:
   - **Scenario**: A user attempts to create a Course without providing a name or level.
   - **Test**: Ensure the application returns a validation error indicating that both fields are required.

3. **Retrieving Course Data**:
   - **Scenario**: A user requests the data of a specific Course by ID.
   - **Test**: Confirm that the Course details returned include both name and level attributes.

4. **Database Migration Verification**:
   - **Scenario**: Check after the migration to ensure the new Course table is created and existing Student data is preserved.
   - **Test**: Validate that the migration did not affect any existing tables or their data.

## Functional Requirements
1. **Course Creation**:
   - Endpoint: `POST /courses`
   - Request Body:
     ```json
     {
       "name": "string" (required),
       "level": "string" (required)
     }
     ```
   - Response:
     - Success (201 Created):
       ```json
       {
         "id": "integer",
         "name": "string",
         "level": "string"
       }
       ```
     - Error (400 Bad Request):
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name and level are required."
         }
       }
       ```

2. **Retrieve Course by ID**:
   - Endpoint: `GET /courses/{id}`
   - Response:
     - Success (200 OK):
       ```json
       {
         "id": "integer",
         "name": "string",
         "level": "string"
       }
       ```
     - Error (404 Not Found):
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Course not found."
         }
       }
       ```

3. **Database Schema**:
   - Update the database schema to include a new `Course` table with the following attributes:
     - `id`: Unique identifier (integer, auto-incremented)
     - `name`: Name of the course (string, required)
     - `level`: Level of the course (string, required)

   - Ensure that the database migration retains all existing data in the Student table.

## Success Criteria
- The application can successfully create a Course with both name and level, returning a valid JSON response indicating success that includes the new attributes.
- The application can retrieve a Course by its ID, and the response must now also include the name and level attributes.
- Validation errors are correctly returned when required fields are missing.
- No existing Student records are impacted during the schema migration; existing data should remain intact.

## Key Entities
- **Course**:
  - Attributes:
    - `id`: Unique identifier (integer, auto-incremented)
    - `name`: Name of the course (string, required)
    - `level`: Level of the course (string, required)

## Assumptions
- Users have a basic understanding of how to use the API to include the new Course.
- The existing database structure allows for the addition of new tables without disruption.
- The application can manage schema changes effectively without requiring downtime for the end-users.

## Out of Scope
- Any modifications to other entities or interfaces that interact with the Course entity.
- Advanced course validation beyond ensuring required fields are present.
- User roles, permissions, or advanced functionalities concerning courses will be addressed in future sprints, if needed.