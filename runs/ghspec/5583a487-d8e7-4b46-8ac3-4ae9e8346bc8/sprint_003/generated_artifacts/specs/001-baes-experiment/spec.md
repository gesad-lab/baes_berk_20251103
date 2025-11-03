# Feature: Create Course Entity

## Overview & Purpose
The purpose of this feature is to introduce a new Course entity to the existing system, allowing the management of courses that students can enroll in. Each Course will have a name and a level, both of which are required fields. This enhancement is expected to enrich the educational management capabilities of the system by enabling better organization and categorization of course offerings, following the previous sprint's improvement focused on enhancing student records with an email field.

## User Scenarios & Testing
1. **Scenario: Create a New Course**
   - **Given** an administrator is on the create course page
   - **When** they enter a valid course name and a valid level, then submit the form
   - **Then** the application should save the course record with both the name and level, returning a success message in JSON format.

2. **Scenario: Validate Input on Course Creation**
   - **Given** an administrator is on the create course page
   - **When** they submit the form without entering a name or level
   - **Then** the application should return an error message indicating that both the name and level fields are required, in JSON format.

3. **Scenario: Retrieve Course Information**
   - **Given** a user requests the course information
   - **When** they send a GET request to retrieve course records
   - **Then** the application should return a list of course records including names and levels in JSON format.

### Testing
- Automated tests should be developed to cover each of the scenarios listed above to ensure that the application behaves as expected when handling course records with the new Course entity.

## Functional Requirements
1. **API Endpoints**:
   - `POST /courses`: Creates a new course record. Must include both the `name` and `level` fields in the request body.
   - `GET /courses`: Returns a list of all course records including `name` and `level` in JSON format.

2. **Input Validation**:
   - The `name` field is required and must be a string.
   - The `level` field is required and must be a string.

3. **Database Management**:
   - Create a new Course table in the database schema with the following fields:
     - `name`: String (required)
     - `level`: String (required)
   - Ensure that the new table is created in a way that does not impact or alter existing Student data during the migration process.

4. **Response Format**:
   - All API responses should return in JSON format, containing course information including both name and level.

## Success Criteria
- The application allows the creation of course records that must include both `name` and `level`, ensuring that:
  - Successfully created course records return a confirmation with the correct status code (201 Created).
  - Retrieval of course records returns a list containing both names and levels with a status code of 200 OK.
  - Invalid requests (e.g., missing name or level) receive appropriate error responses with clear messages and a status code of 400 Bad Request.
- The application initializes the updated database schema with the new Course table on startup without errors.
- Automated tests achieve at least 70% coverage for business logic, confirming functionality across all scenarios related to Course creation and retrieval.

## Key Entities
- **Course**:
  - `name`: String (required)
  - `level`: String (required)

## Assumptions
- Users have the appropriate permissions to create courses within the application.
- The application assumes that user input for both `POST` and `GET` requests will be submitted in JSON format.
- The level provided for courses will be in a standard text format.

## Out of Scope
- The implementation of features allowing the updating or deleting of course records will not be included in this iteration.
- This specification will not cover advanced functionalities related to course prerequisites or dynamic level types.
- User interfaces beyond the basic course creation and retrieval will not be addressed in this sprint; future enhancements to support such features are acknowledged.