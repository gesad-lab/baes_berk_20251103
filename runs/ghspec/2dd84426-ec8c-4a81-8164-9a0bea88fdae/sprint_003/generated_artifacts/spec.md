# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new `Course` entity to the existing system. This entity will allow the application to manage courses with a designated name and level, thereby enhancing the educational structure and enabling better organization of student enrollments. The implementation of this feature will maintain existing functionalities while ensuring that course-related functionalities can be integrated in the future.

## User Scenarios & Testing
1. **Creating a Course**: A user sends a request to create a course with valid values for both `name` and `level`. The system should return a success response with the created course details, including both fields.
2. **Failing to Create a Course with Missing Fields**: A user sends a request to create a course with a valid name but without a level. The application should return an error response indicating that the level field is required.
3. **Retrieving All Courses**: A user requests to retrieve all courses from the database. The application should return a JSON array of all course objects, including their names and levels.
4. **Database Migration**: Upon starting the application, the database schema must be updated to include the new `Course` table without impacting existing `Student` data.

## Functional Requirements
1. **Create a Course**:
   - Endpoint: `POST /courses`
   - Request Body: `{ "name": "string", "level": "string" }` (both required)
   - Response: `201 Created` with the created course object in JSON, which includes the name and level.

2. **Retrieve All Courses**:
   - Endpoint: `GET /courses`
   - Response: `200 OK` with a JSON array of course objects containing both names and levels.

3. **Database Migration**:
   - The database schema must be updated to introduce a new table, `Course`, with fields for `name` and `level`.
   - The migration must preserve existing data within the `Student` entity.

## Success Criteria
- The system must return a `201 Created` response when a course is successfully created with both name and level.
- The system must return a `400 Bad Request` error with a message indicating that the level is required if a create request is missing the level.
- The system must return a `200 OK` response with an array of course data including names and levels when the user retrieves all courses.
- The database schema must include the `Course` table after migration, and the process must not cause any data loss.

## Key Entities
- **Course**
  - **name**: String (required)
  - **level**: String (required)

## Assumptions
- The new course names and levels will be valid strings that conform to expected naming conventions.
- The application will maintain its existing architecture and functionality, including no changes to authorization or authentication features.
- The database management system allows for the addition of new tables and schemas without interfering with existing data.

## Out of Scope
- User interface modifications or frontend changes for displaying or interacting with courses are not included in this specification.
- Advanced features such as course categories, prerequisites, or scheduling are not addressed in this feature.
- Functionality to validate the uniqueness of course names or levels is not included in this scope.