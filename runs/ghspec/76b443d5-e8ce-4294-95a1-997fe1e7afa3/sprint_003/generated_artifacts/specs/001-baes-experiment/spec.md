# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new Course entity that includes a name and level field. This enhancement will allow the system to manage courses alongside students, providing the ability to associate students with specific courses, and ultimately enriching the educational data model. By having this structured data, the application can better support course management functions, including student enrollment and course listings.

## User Scenarios & Testing
1. **Scenario 1: Create a new Course**
   - **Given** the user provides a name and a level for a new Course,
   - **When** the user submits a request to create the Course,
   - **Then** the Course should be created, and a successful response with the Course data (including id, name, and level) should be returned.

2. **Scenario 2: Retrieve Course details**
   - **Given** an existing Course ID,
   - **When** the user requests the details of that Course,
   - **Then** the response should contain the Course's name and level.

3. **Scenario 3: Create a Course without a name**
   - **Given** the user submits a request without providing a name,
   - **When** the application processes the request,
   - **Then** the response should indicate that the name is required.

4. **Scenario 4: Create a Course without a level**
   - **Given** the user submits a request without providing a level,
   - **When** the application processes the request,
   - **Then** the response should indicate that the level is required.

## Functional Requirements
1. The application must include an API endpoint to create a new Course with the following:
   - Method: POST
   - Endpoint: `/courses`
   - Request Body: JSON object containing "name" (string, required) and "level" (string, required).
   - Response: JSON object containing the created Course's data, including an auto-generated ID, name, and level.

2. The application must include an API endpoint to retrieve a Course by ID with the following:
   - Method: GET
   - Endpoint: `/courses/{id}`
   - Response: JSON object containing the Course's data (ID, name, level).

3. The application must update the database schema to include the new Course table with necessary migration steps ensuring existing Student data is preserved.

4. The application must validate that both the name and level fields are present when creating a Course.

5. The API must always respond with valid JSON, including error responses.

## Success Criteria
1. The application should successfully create a Course record when provided with valid name and level.
2. The application should return a JSON response that contains the correct Course details upon retrieval by ID.
3. An error response indicating the missing name must be returned when attempting to create a Course without a name.
4. An error response indicating the missing level must be returned when attempting to create a Course without a level.
5. The database schema should successfully update on startup without losing any existing Student data.

## Key Entities
- **Course**
  - **ID** (auto-generated integer)
  - **name** (string, required)
  - **level** (string, required)

## Assumptions
1. The existing system is fully operational and will support the addition of new entities without issues.
2. Users will be able to send API requests using tools such as Postman or cURL for testing purposes.
3. The application will maintain input validation for new entity fields to ensure data quality.
4. The tech stack used in the previous sprint remains consistent for this increment.

## Out of Scope
1. Any user interface changes for Course management.
2. Advanced features such as updating or deleting Course records beyond the creation of the entity.
3. Integrations with external course management systems.
4. Deployment to a production environment; this focus is on local development and testing.