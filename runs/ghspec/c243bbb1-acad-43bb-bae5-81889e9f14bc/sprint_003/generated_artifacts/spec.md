# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to add a new entity, Course, into the existing system. This will allow users to create and manage courses with attributes such as name and level, enabling a structured approach to course management. This feature is critical for enhancing educational data management and will lay the groundwork for future functionalities like course enrolment and associations with students.

## User Scenarios & Testing
1. **Creating a New Course**:
   - A user sends a POST request to the `/courses` endpoint with a valid name and level.
   - Expected Result: A new course entity is created in the database, and a success message is returned in JSON format.

2. **Retrieving All Courses**:
   - A user sends a GET request to the `/courses` endpoint.
   - Expected Result: A JSON response containing a list of all course entities, each with its name and level.

3. **Handling Missing Name or Level**:
   - A user sends a POST request to the `/courses` endpoint without a name or level.
   - Expected Result: An error message is returned indicating that both fields are required.

## Functional Requirements
1. The application must expose the following API endpoints for the Course entity:
   - **POST `/courses`**: Create a new course. 
     - **Request Body**:
       - `name`: string (required)
       - `level`: string (required)
     - **Response**: JSON object including a success message and the created course data.

   - **GET `/courses`**: Retrieve a list of all courses.
     - **Response**: JSON array of course objects, where each object contains a name and level.

2. The application must update the existing database schema on startup to include the new Course table with the following attributes:
   - `id`: int (auto-generated primary key)
   - `name`: string (required)
   - `level`: string (required)

3. The application must return JSON responses for all course-related API requests and perform input validation to ensure that:
   - Both `name` and `level` fields are provided when creating a course.

## Success Criteria
- The Course entity must be successfully created with valid name and level, responding within 200 milliseconds.
- The application must successfully retrieve and return a list of all courses in JSON format, also within the same response time threshold.
- It should handle missing fields by returning appropriate error messages with a `400 Bad Request` status.
- A migration process must be executed to ensure the new Course table is added without affecting existing data, particularly the Student data.
- The application should operate in a development environment without configuration errors.

## Key Entities
- **Course**:
  - **Attributes**:
    - `id`: int (auto-generated primary key)
    - `name`: string (required)
    - `level`: string (required)

## Assumptions
- Existing student data remains unaffected by the new course entity and migration.
- Users interacting with the API have a basic understanding of how to send HTTP requests.
- The application will run in a controlled environment where the necessary infrastructure is set up.

## Out of Scope
- User interface for course management; this feature focuses on API functionality.
- Advanced error handling and logging mechanisms are outside the scope of this implementation.
- Integration with external education systems or platforms regarding course content delivery is not included in this scope.