# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` entity and the newly created `Teacher` entity. By enabling courses to be associated with specific teachers, the overall functionality of the application can be enhanced, which will allow for better management of course assignments and educator accountability. This relationship will facilitate user queries and reporting on courses linked to teachers, thus improving the educational data organization within the system.

## User Scenarios & Testing
1. **Scenario: Assign a Teacher to a Course**
   - **Given** I want to assign a teacher to a specific course
   - **When** I update the course with a teacher ID
   - **Then** the course should show the assigned teacher information.

2. **Scenario: Validate Course Creation with Teacher Assignment**
   - **Given** I want to create a new course and assign a teacher
   - **When** I send a POST request to the `/courses` endpoint with course details and a teacher ID
   - **Then** the course should be created with the specified teacher assignment, and I should receive a success response.

3. **Scenario: Assign a Non-existent Teacher to a Course**
   - **Given** I attempt to assign a teacher ID that does not exist
   - **When** I update the course with that teacher ID
   - **Then** I should receive an error response indicating that the teacher does not exist.

## Functional Requirements
1. **Course Entity Update**:
   - Update the existing `Course` entity to include a relationship to the `Teacher` entity.
   - Add a new field to the existing `Course` structure:
     - `teacher_id`: Integer (Foreign Key referencing Teacher entity)

2. **API Endpoints Modifications**:
   - **POST /courses**: Create a new course with an optional teacher assignment.
     - Request Body: `{ "course_name": "string", "teacher_id": "integer" }`
     - Response: `{ "message": "Course created successfully." }` (Status Code: 201 Created)
   
   - **PUT /courses/{id}**: Update an existing course to assign a teacher.
     - Request Body: `{ "teacher_id": "integer" }`
     - Response: `{ "message": "Course updated successfully." }` (Status Code: 200 OK)
     - Error Response: `{"error": {"code": "E003", "message": "Teacher does not exist."}}` (Status Code: 400 Bad Request)

3. **Database Schema Update**:
   - Update the existing database schema to include a new column in the `Course` table:
     - `teacher_id`: Integer (Foreign Key referencing `Teacher` entity; can be null).

4. **Database Migration**:
   - The migration process must ensure that existing `Student` and `Course` data remains preserved after adding the new `teacher_id` column.
   - Existing courses should be updated in place, with `teacher_id` set to null initially.

## Success Criteria
- The application starts without errors, and the `Course` table includes the new `teacher_id` field.
- Successfully creating a course with a valid teacher ID returns a status code of 201 Created along with a success message.
- Updating a course to assign a teacher succeeds when provided with a valid teacher ID, returning a status code of 200 OK.
- Proper error handling returns appropriate status codes and messages when attempting to assign a non-existent teacher.
- The migration preserves existing data in both the `Student` and `Course` tables without loss.

## Key Entities
- **Course**:
  - `id`: Integer (Primary Key)
  - `course_name`: String (not null)
  - `teacher_id`: Integer (Foreign Key referencing Teacher entity; can be null)

- **Teacher** (Previous Entity):
  - `id`: Integer (Primary Key)
  - `name`: String (not null)
  - `email`: String (not null, unique)

## Assumptions
- Teacher IDs assigned to courses exist in the `Teacher` table.
- Course names will not exceed standard character limits for database entries.
- Relationships between teachers and courses can be optional (i.e., a course may not have a teacher assigned).

## Out of Scope
- User interface modifications for displaying teacher assignments on course pages are not included in this specification.
- Functionality for removing or replacing an assigned teacher is not covered in this sprint.
- Reporting functionalities to display courses by assigned teachers or teacher performance metrics are outside the scope of this implementation.