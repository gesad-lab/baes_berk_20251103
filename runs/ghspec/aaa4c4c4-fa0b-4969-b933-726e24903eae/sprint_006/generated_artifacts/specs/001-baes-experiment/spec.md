# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity within the existing educational system. By allowing each course to have a designated teacher, this feature aims to enhance the management of courses and their associated educators. This relationship is essential for streamlining interactions between teachers and courses, thereby improving the functionality of the application and supporting its growth in educational management capabilities.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**:
   - A user submits a `PUT` request to update a course, providing the course ID and the ID of the teacher to be assigned.
   - The application should return a JSON response confirming the successful assignment, including the course and teacher details.

2. **Retrieving Course Information with Teacher**:
   - A user sends a `GET` request to retrieve details of a specific course by its ID.
   - The application should return a JSON object containing the course details, including the assigned teacher's information.

3. **Handling Errors for Invalid Teacher Assignments**:
   - A user attempts to assign a teacher to a course that does not exist.
   - The application should respond with an appropriate error message indicating the course was not found and validating the input accordingly.

### Testing
- **Unit Tests**: Verify the assignment of teacher data to course records.
- **Integration Tests**: Ensure the application endpoints function correctly when interacting with both Course and Teacher entities.
- **API Response Tests**: Confirm the correctness of the returned data structure for courses that include teacher details.

## Functional Requirements
1. **Assign Teacher to Course**:
   - Endpoint: `PUT /courses/{course_id}/assign-teacher`
   - Request Body: JSON object containing `{"teacher_id": "<teacher_id>"}`.
   - Response: JSON object confirming success, including the updated course details with the teacher assigned.

2. **Get Course Details with Teacher Information**:
   - Endpoint: `GET /courses/{course_id}`
   - Response: JSON object containing course details, including the assigned teacher’s ID, name, and email.

3. **Error Responses**:
   - If a request to assign a teacher fails due to a non-existent course, respond with a `404 Not Found` status and a JSON message explaining that the course does not exist.
   - If a request misses required data (teacher ID), respond with a `400 Bad Request` status and a JSON message indicating the missing field.

4. **Database Migration**:
   - The application must include a migration step that updates the existing database schema to include a foreign key in the Course table that references the Teacher entity while preserving the existing Student, Course, and Teacher data.

## Success Criteria
- The application successfully allows assigning a teacher to a course and retrieves course information with teacher details.
- The application returns appropriate HTTP status codes and JSON messages for both successful and erroneous requests.
- Existing records for students and courses remain unaffected during the migration process, ensuring data integrity.
- The database schema is updated to include the relationship between Course and Teacher without manual intervention.

## Key Entities
- **Teacher**:
  - `id`: Integer (auto-increment, primary key)
  - `name`: String (required)
  - `email`: String (required, must be unique)

- **Student**:
  - `id`: Integer (auto-increment, primary key)
  - `name`: String (required)
  - `courses`: List of Course IDs (foreign key relationship to Course entity)

- **Course**:
  - `id`: Integer (auto-increment, primary key)
  - `name`: String (required)
  - `level`: String (required)
  - `teacher_id`: Integer (foreign key relationship to Teacher entity, nullable to allow for courses without assigned teachers)

## Assumptions
- Users are familiar with using API tools to interact with the system.
- The application will maintain consistent handling of data based on the provided specifications.
- Teacher IDs will be validated to ensure they correspond to existing teacher records when assigning them to courses.

## Out of Scope
- Modifying existing functionalities unrelated to course-teacher relationships.
- Implementing advanced features such as multi-teacher assignments for single courses or detailed reporting systems based on course/teacher interactions.
- Changes to the user interface pertaining to course management beyond the API's request and response structures.

## Instructions for Incremental Development:
1. Extend the existing system by adding the teacher relationship to the Course entity without removing or altering existing structures for Students and Courses.
2. Utilize the same technology and structure as outlined in the previous sprint for consistency, maintaining data integrity throughout the process.
3. Ensure that all new components—for the course-teacher relationship—integrate seamlessly with existing functionalities related to Courses and Teachers.
4. Document all necessary modifications to current operations that facilitate the addition of the new teacher relationship while preserving existing functionality.