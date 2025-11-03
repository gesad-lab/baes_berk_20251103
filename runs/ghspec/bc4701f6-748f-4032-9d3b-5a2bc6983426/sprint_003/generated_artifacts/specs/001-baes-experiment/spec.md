# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to establish a new Course entity within the existing application that includes fields for the course name and level. This enhancement will allow the system to organize and manage courses effectively, contributing to improved functionality in course-related processes, data management, and user experience. This feature aims to align with the application's goals of providing comprehensive educational resources and management tools.

## User Scenarios & Testing
1. **Creating a Course**: 
   - A user sends a POST request to create a new course, including the name and level in the request body.
   - The application should create a new course record with the provided details and return a success message along with the created course’s details.

2. **Retrieving Course Details**:
   - A user sends a GET request to retrieve course information by its unique identifier.
   - The application should return the course details in JSON format, including the name and level.

3. **Error Handling - Missing Fields**:
   - A user sends a POST request with missing or empty name or level fields.
   - The application should respond with an appropriate error message indicating that each field is required.

4. **Database Schema Update**:
   - Upon application startup, the database schema should be updated to include the new Course table while preserving existing Student data.

## Functional Requirements
1. **Endpoint for Creating a Course**:
   - Method: POST
   - URL: `/courses`
   - Request body:
     - `name`: string (required)
     - `level`: string (required)
   - Response: 
     - `201 Created` on success with the created course's details, including name and level, returned as JSON.

2. **Endpoint for Retrieving a Course**:
   - Method: GET
   - URL: `/courses/{id}`
   - Response:
     - `200 OK` with the course’s details, including name and level, in JSON if found.
     - `404 Not Found` if the course does not exist.

3. **Automatic Database Schema Update**:
   - On application startup, automatically update the database schema to include the new Course table while maintaining existing Student data.

4. **Error Handling**:
   - Return appropriate error messages with status codes for invalid requests, such as `400 Bad Request` for missing name or level.

## Success Criteria
1. **Functionality Extension**:
   - The application allows users to create and retrieve course records, including the new name and level fields.
2. **Response Format**: 
   - The API consistently returns JSON formatted responses for success and error scenarios, including the new course fields.
3. **Schema Update**:
   - The database schema is automatically updated on application startup without manual intervention, preserving all existing Student data.
4. **Error Handling**:
   - The application correctly responds to invalid course creation attempts with clear and actionable error messages regarding the missing fields.

## Key Entities
- **Course**:
  - **Fields**:
    - `id`: Integer (auto-generated, primary key)
    - `name`: String (required)
    - `level`: String (required)

## Assumptions
- The application remains hosted in an environment supporting the requirements established in earlier sprints.
- Users will continue to have client software capable of sending HTTP requests (e.g., Postman, web browser).
- The application will run locally for testing; production deployment will be defined later.
- The existing data in the Student table will remain unaffected by the introduction of the new Course table.

## Out of Scope
- User authentication and authorization mechanisms specific to the Course entity.
- Validation or formatting checks for names and levels beyond ensuring they are non-empty strings.
- Additional fields or entities beyond the Course entity.
- User interfaces beyond the API endpoints (e.g., frontend web pages).
- Integration with other data sources beyond the SQLite database required for persistence.