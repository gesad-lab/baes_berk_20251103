# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to create a new `Course` entity within the application, allowing for the management of courses that students can enroll in. This enhancement facilitates better organization of educational offerings, making it easier to assign courses to students and track their enrollment. By capturing details about each course, the application will improve the educational experience for both students and administrators.

## User Scenarios & Testing
1. **Scenario 1: Create a Course**  
   - **Given**: An administrator has access to the course management functionality within the application.  
   - **When**: The administrator submits a form with a name and level for a new course.  
   - **Then**: The course should be created in the database, including the name and level, and a JSON response should return indicating success.

2. **Scenario 2: Retrieve a List of Courses**  
   - **Given**: An administrator accesses the course management functionality.  
   - **When**: The administrator requests to view all courses.  
   - **Then**: A JSON response should display a list of all courses with their respective names and levels.

3. **Scenario 3: Handle Missing Course Name**  
   - **Given**: An administrator attempts to create a course without a name.  
   - **When**: The administrator submits the form.  
   - **Then**: A JSON error response should indicate that the course name is required.

4. **Scenario 4: Handle Missing Course Level**  
   - **Given**: An administrator attempts to create a course without a level.  
   - **When**: The administrator submits the form.  
   - **Then**: A JSON error response should indicate that the course level is required.

## Functional Requirements
1. **Course Entity Creation**  
   - A new `Course` entity must be introduced with the following attributes:
     - `name`: String (required)
     - `level`: String (required)

2. **Database Schema Update**  
   - The database schema must be modified to include the new `Course` table with the specified fields while ensuring that the addition does not affect existing `Student` data.

3. **API Endpoints**  
   - **POST /courses**: Accepts a JSON object to create a new course.  
     - Request Body: `{ "name": "string", "level": "string" }`
     - Response: JSON success message with course information or an error message if validation fails.
  
   - **GET /courses**: Returns a list of all courses in JSON format.  
     - Response: `[ { "name": "string", "level": "string" }, ... ]`

4. **Database Migration**  
   - Implement a migration to create the `Course` table with `name` and `level` fields without affecting existing data in the `Student` table.

5. **JSON Responses**  
   - All API responses must be formatted in JSON, including details of the course entity after creation.

## Success Criteria
- The application must return a status of 200 OK for successful requests to create and retrieve courses and appropriate error codes for failed requests related to required fields.
- A new course can be successfully created with a valid name and level, resulting in a success response that includes both course attributes.
- A list of all created courses can be retrieved, and all course names and levels should be displayed in the response.
- Attempts to create a course without a name or level should return detailed error responses indicating the respective validation issues.

## Key Entities
- **Course**  
  - Attributes:  
    - `id`: Integer (auto-generated ID for each course)  
    - `name`: String (required)  
    - `level`: String (required)

## Assumptions
- Users accessing the course management functionality have basic familiarity with web forms.
- The application must validate that both the name and level fields are provided on course creation.
- Existing infrastructure, including the database and application frameworks, will support the addition of new entities without major changes.

## Out of Scope
- User authentication and authorization management related to course creation or retrieval.
- Advanced features such as editing or deleting course records.
- Any updates to the front-end interface beyond the specified API endpoints.
- Handling of relationships between courses and other entities, such as students or instructors.