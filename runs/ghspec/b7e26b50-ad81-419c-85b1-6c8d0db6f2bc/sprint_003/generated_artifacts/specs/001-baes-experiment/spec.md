# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity within the application, allowing us to capture essential information about courses offered. Each Course will have a required name and level, which will enhance the structure of our educational offerings and facilitate better course management. This addition aligns with user needs for a more organized catalog of courses and supports future functionalities related to course enrollment and tracking.

## User Scenarios & Testing
1. **User Scenario: Create New Course**
   - As a user, I want to be able to create a new course entry with a name and level, so that I can manage courses effectively.
   - **Test**: Verify that a POST request to the `/courses` endpoint with valid name and level returns a success message and saves the course in the database.

2. **User Scenario: Missing Course Data**
   - As a user, if I submit a course entry without a name or level, I want to receive a clear error message explaining the issue.
   - **Test**: Verify that a POST request with missing name or level returns a 400 error status and an appropriate error message.

3. **User Scenario: Fetch Course Details**
   - As a user, I want to view the details of a specific course to understand its attributes.
   - **Test**: Verify that a GET request to the `/courses/{id}` endpoint returns the correct course details in JSON format.

## Functional Requirements
1. **Create Course**
   - Endpoint: `POST /courses`
   - Request Body:
     - `name`: string, required
     - `level`: string, required
   - Response:
     - 201 Created with a JSON message confirming the course has been created, including its ID.

2. **Fetch Course Details**
   - Endpoint: `GET /courses/{id}`
   - Response:
     - 200 OK with a JSON object containing the course details, including `id`, `name`, and `level`.

3. **Error Handling**
   - If the request does not contain a name or level, respond with:
     - 400 Bad Request and a JSON error message stating "Name is required." or "Level is required."

4. **Database Schema Update**
   - The existing database schema must be updated to include a new `Course` table with the following fields:
     - `id`: integer, primary key, auto-increment
     - `name`: string, required
     - `level`: string, required
   - A database migration must be created to incorporate this new table without affecting existing Student data.

## Success Criteria
- The application can successfully create and retrieve course entries, including their names and levels, without errors.
- The application returns appropriate success and error messages in JSON format.
- Cover at least 70% of business logic with automated tests, particularly for endpoints handling course creation and retrieval.
- Ensure that the database migration does not result in data loss, preserving existing Student records and relationships.

## Key Entities
- **Course**
  - Attributes:
    - `id` (integer, primary key, auto-increment)
    - `name` (string, required)
    - `level` (string, required)

## Assumptions
- It is assumed that the level of the course includes common categories such as "Beginner", "Intermediate", and "Advanced".
- The application will run in a development environment with SQLite as the database, consistent with previous sprints.
- Users accessing the application have the authority to manage course information as required.

## Out of Scope
- Any changes or features related to actual course enrollment, scheduling, or instructor assignments are outside the scope of this feature.
- Additional attributes or functionalities for the Course entity beyond the name and level are not included in this specification.