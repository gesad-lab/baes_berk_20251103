# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing application. This enhancement will allow each Student to enroll in multiple Courses, thereby enriching the data model and improving educational management capabilities. Enabling this relationship aligns with the application's goals of providing comprehensive educational resources and facilitating better academic tracking for users.

## User Scenarios & Testing
1. **Enrolling a Student in a Course**: 
   - A user sends a POST request to enroll a student in a course, including the student ID and course ID in the request body.
   - The application should link the specified student to the specified course and return a success message along with the updated student’s details including their courses.

2. **Retrieving a Student's Courses**:
   - A user sends a GET request to find all courses a student is enrolled in by their unique student ID.
   - The application should return the list of courses associated with the student in JSON format.

3. **Error Handling - Non-existent Course or Student**:
   - A user sends a POST request with a student ID or course ID that does not exist.
   - The application should respond with an appropriate error message indicating that the course or student is not found.

4. **Database Schema Update**:
   - Upon application startup, the database schema should be updated to include a join or mapping table that preserves existing Student and Course data while establishing their relationship.

## Functional Requirements
1. **Endpoint for Enrolling a Student in a Course**:
   - Method: POST
   - URL: `/enrollments`
   - Request body:
     - `student_id`: Integer (required)
     - `course_id`: Integer (required)
   - Response: 
     - `201 Created` on success with the updated student’s details, including their courses, returned as JSON.

2. **Endpoint for Retrieving a Student's Courses**:
   - Method: GET
   - URL: `/students/{student_id}/courses`
   - Response:
     - `200 OK` with the list of courses the student is enrolled in, if found.
     - `404 Not Found` if the student does not exist.

3. **Automatic Database Schema Update**:
   - On application startup, automatically update the database schema to include a join or mapping table that links students to their enrolled courses while maintaining all existing data.

4. **Error Handling**:
   - Return appropriate error messages with status codes for invalid requests, such as `400 Bad Request` for missing student or course IDs, and `404 Not Found` for non-existent students or courses.

## Success Criteria
1. **Functionality Extension**:
   - The application allows users to enroll students in courses and retrieve the list of courses associated with each student.
2. **Response Format**: 
   - The API consistently returns JSON formatted responses for success and error scenarios, including the updated student course relations.
3. **Schema Update**:
   - The database schema is automatically updated on application startup without manual intervention, preserving all existing data in the Student and Course entities.
4. **Error Handling**:
   - The application correctly responds to invalid enrollment attempts with clear and actionable error messages regarding the invalid IDs.

## Key Entities
- **Enrollment** (Mapping Table):
  - **Fields**:
    - `student_id`: Integer (foreign key to Student entity)
    - `course_id`: Integer (foreign key to Course entity)

## Assumptions
- The application will operate in the same environment as earlier sprints, ensuring the database supports the necessary schema updates.
- Users have client software capable of sending HTTP requests.
- The existing data in the Student and Course tables will remain unaffected by the introduction of the enrollment mapping.
- Existing user and course data is correctly formatted and does not require additional validation.

## Out of Scope
- User authentication and authorization mechanisms specific to the enrollment process.
- Validation or formatting checks for student and course IDs beyond verifying existence in respective tables.
- Additional features for modifying or deleting course enrollments.
- User interfaces beyond the API endpoints (e.g., frontend web pages).
- Integration with external systems or databases beyond the current scope.