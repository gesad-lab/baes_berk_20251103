# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new Course entity within the system to facilitate the organization and management of courses offered by the educational institution. This addition will enhance the capability to manage educational programs, allowing for better categorization and tracking of courses. By incorporating a Course entity with a name and level fields, the application will support academic planning and student enrollment activities more effectively.

## User Scenarios & Testing
1. **Creating a Course**:
   - Given the user has access to the application, when they submit a valid name and level for a new course, then a new course record with both the name and level should be created in the database.

2. **Retrieving Course Information**:
   - Given the user requests a course by ID, when the course exists in the database, then the application should return the course's name and level in JSON format.

3. **Updating Course Information**:
   - Given the user has requested to update a course's name or level, when they provide a valid ID and new values, then the corresponding course's information should be updated in the database.

4. **Error Handling for Course Fields**:
   - Given the user submits invalid input for course creation (like empty name or level fields), then the application should return a clear error message indicating the input requirements.

## Functional Requirements
1. **Create Course**:
   - Endpoint: POST /courses
   - Request Body: JSON object containing "name" (string, required) and "level" (string, required).
   - Response: 201 Created with the created course object in JSON format.

2. **Retrieve Course**:
   - Endpoint: GET /courses/{id}
   - Response: 200 OK with the course object including "name" and "level" in JSON format, or 404 Not Found if the ID does not exist.

3. **Update Course**:
   - Endpoint: PUT /courses/{id}
   - Request Body: JSON object containing "name" (string, optional) and "level" (string, optional).
   - Response: 200 OK with the updated course object including the new name or level values, or 404 Not Found if the ID does not exist.

4. **Database Schema**:
   - A new "courses" table should be created in the database with the following columns:
     - name: String, required field to store course names.
     - level: String, required field to store the academic level of the course.

## Success Criteria
- The application must respond correctly to all endpoints related to creating, retrieving, and updating courses as specified above.
- Both the name and level fields must be validated, ensuring they are provided and not empty, with at least 90% test coverage for creating, updating, and retrieving courses.
- The database schema should be updated to include the new courses table without impacting any existing data in the students table.

## Key Entities
- **Course**:
  - id: Integer, auto-generated primary key.
  - name: String, required field to store course names.
  - level: String, required field to store the academic level of the course.

## Assumptions
- The application will follow similar validation procedures as established with the Student entity for ensuring required fields are present.
- Users are familiar with how to interact with RESTful APIs for managing course records.
- The application will be deployed in an environment compatible with the current tech stack utilized in previous sprints.

## Out of Scope
- Advanced features related to course scheduling or enrollment; this feature focuses solely on the creation and management of course records.
- User interface changes to accommodate course management; only backend functionality is included in this specification.
- Integration with any external course management systems or tools; this feature will operate independently within the existing framework.