# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity that allows for the categorization of educational subjects. Each course will have a name and a level, which are essential attributes for organizing the curriculum and enhancing the educational experience for students. By implementing courses, the system will provide a structured way to enroll students and manage their academic progression.

## User Scenarios & Testing
1. **Scenario 1: Create a New Course**
   - User sends a request to add a new course with a valid name and level.
   - Expected Outcome: The system should successfully create the course and return a JSON response containing the course’s information, including an auto-generated ID.

2. **Scenario 2: Create Course with Missing Name**
   - User sends a request to add a new course without a name but with a valid level.
   - Expected Outcome: The system should return a JSON error response indicating that the name field is required.

3. **Scenario 3: Create Course with Missing Level**
   - User sends a request to add a new course with a valid name but without a level.
   - Expected Outcome: The system should return a JSON error response indicating that the level field is required.

4. **Scenario 4: Retrieve Course Information**
   - User sends a request to retrieve a list of all courses.
   - Expected Outcome: The system should return a JSON response with an array of all existing courses, showing their IDs, names, and levels.

5. **Scenario 5: Database Migration Verification**
   - On application startup or during migration, the database schema should be updated to include the Course table.
   - Expected Outcome: The system should successfully apply the migration while preserving existing Student data.

## Functional Requirements
1. **API Endpoints**:
   - **POST /courses**: Create a new course with a JSON body containing the name and level.
   - **GET /courses**: Retrieve a list of all courses including their IDs, names, and levels.

2. **Database Schema Changes**:
   - Create a new Course table with the following attributes:
     - id: integer (auto-incrementing primary key)
     - name: string (required)
     - level: string (required)

3. **Responses**:
   - All API responses must return in JSON format.
   - Successful course creation should return status code `201 Created`.
   - Retrieval should return status code `200 OK` with courses' data.
   - Validation errors for missing fields should return status code `400 Bad Request`.

## Success Criteria
- The application must allow for the creation of a course with name and level, ensuring both fields are required.
- The application must successfully retrieve and list all courses without errors.
- The database schema must include the new Course table while preserving all existing Student data.
- All responses issued by the API endpoints must be in a valid JSON format.

## Key Entities
- **Course**:
  - Attributes:
    - id: integer (auto-incrementing primary key)
    - name: string (required)
    - level: string (required)

## Assumptions
- The user has access to the same environment and tech stack used in the previous sprint.
- The existing SQLite database can be updated to include the new Course table without losing existing Student data through a proper migration process.
- Users can interact with the updated RESTful API and understand JSON data formats.

## Out of Scope
- Modifications to authentication or authorization mechanisms.
- Functions related to updating or deleting course records.
- Additional features for managing course content beyond storing the name and level.
- User interface changes in frontend applications, if applicable.
- Any logic related to enrolling students into courses will not be covered in this feature.