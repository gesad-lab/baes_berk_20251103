# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new Course entity in our existing database schema that will allow the system to manage courses. The addition of a Course entity with name and level fields will not only enrich our educational data model but also facilitate future functionalities related to course management, such as linking courses to students or instructors.

## User Scenarios & Testing
### User Scenarios
1. **Creating a Course**:
   - As a user, I want to create a new Course by providing its name and level so that I can catalog courses within the system.

2. **Retrieving Courses**:
   - As a user, I want to retrieve a list of all Courses to understand the available options for student enrollment.

3. **Error Handling**:
   - As a user, I want to be notified if I attempt to create a Course without providing the required name or level so that I can correct my input.

### Testing
1. Test the creation of a Course with valid name and level.
2. Test the response when trying to create a Course without a name or level.
3. Test the retrieval of all Courses to ensure they are returned in JSON format with corresponding name and level.

## Functional Requirements
1. **Create Course**:
   - Endpoint: POST `/courses`.
   - Input: A JSON object containing required fields `name` (string) and `level` (string).
   - Output: A JSON response confirming that the Course has been created, including a unique identifier.

2. **Retrieve Courses**:
   - Endpoint: GET `/courses`.
   - Output: A JSON array containing all Courses, each with their unique identifier, name, and level.

3. **Database Initialization**:
   - On application startup, the database schema must be updated to include a new `Course` table with the following columns:
     - `id`: Unique identifier (auto-generated).
     - `name`: Required string (non-null).
     - `level`: Required string (non-null).
   - The database migration process should ensure that existing Student data is preserved and unchanged during this schema update.

## Success Criteria (measurable, technology-agnostic)
1. The application must respond with a 201 status code and a confirmation message, including the unique identifier when a Course is successfully created.
2. The application must respond with a 200 status code and a JSON array of Courses, including name and level fields, when the retrieval endpoint is accessed.
3. The application should validate input and respond with a 400 status code and an appropriate error message when an invalid request (e.g., missing name or level) is made.
4. The database must be updated on startup with the new schema reflecting the Course table, while preserving all existing Student data.

## Key Entities
- **Course**:
  - Fields:
    - `id`: Unique identifier (auto-generated).
    - `name`: Required string.
    - `level`: Required string.

## Assumptions
- Users accessing the application are familiar with making API requests (e.g., through tools like Postman or curl).
- The application will be used in a development or small-scale environment where SQLite is appropriate for data persistence, similar to the previous sprint.
- Existing Student entries in the database will remain intact post-migration, and the addition of the Course table will not interfere with their data.

## Out of Scope
- User authentication and authorization for managing Courses.
- Advanced features such as linking Courses to Students or Instructors.
- Frontend components; the focus is solely on the backend API.