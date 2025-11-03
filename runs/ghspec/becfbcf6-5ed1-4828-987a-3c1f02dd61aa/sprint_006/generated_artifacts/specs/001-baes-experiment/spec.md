# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose

The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity in the Student Management Web Application. By adding this relationship, each Course can be assigned a Teacher, enabling better management of educational resources and communication. This feature will facilitate the organization of course assignments and instructor details, which is essential for effective educational administration. The implementation of this feature lays the groundwork for future enhancements that include more advanced functionalities centered around course management and teacher assignments.

## User Scenarios & Testing

1. **Assigning a Teacher to a Course**:
   - **Scenario**: An administrator assigns a teacher to an existing course.
   - **Test**: Verify that the course record updates correctly to reflect the assigned teacher, and this information is retrievable.

2. **Validating Teacher Assignment**:
   - **Scenario**: An administrator attempts to assign a non-existent teacher to a course.
   - **Test**: Verify that the system returns an appropriate error message indicating that the specified teacher does not exist.

3. **Retrieving Course with Teacher Information**:
   - **Scenario**: A user retrieves information about a specific course along with the assigned teacher.
   - **Test**: Verify that the retrieved course data includes accurate details of the assigned teacher.

4. **Database Schema Update**:
   - **Scenario**: The application starts up with the updated schema that establishes the relationship between the Course and Teacher entities.
   - **Test**: Verify that the database schema integrates this relationship without affecting existing Student and Course data.

## Functional Requirements

1. **Add a Teacher ID field to the Course entity**:
   - The Course entity must have a new field:
     - `teacher_id`: Integer (ID of the assigned Teacher)

2. **Implement a database migration**:
   - Update the database schema to add the `teacher_id` field in the existing Course table.
   - Ensure the migration maintains existing integrity of Student, Course, and Teacher data.

3. **Create an endpoint for assigning a Teacher to a Course**:
   - **Method**: PATCH
   - **Endpoint**: `/courses/{course_id}/assign-teacher`
   - **Body**:
     - `teacher_id`: Integer (required)
   - **Response**:
     - JSON object confirming the assignment of the teacher and returning the updated course information.

4. **Create an endpoint for retrieving a Course with Teacher information**:
   - **Method**: GET
   - **Endpoint**: `/courses/{course_id}`
   - **Response**:
     - JSON object containing the Course name, level, and the assigned Teacher's details (name and email).

5. **Ensure all responses are formatted in valid JSON syntax** according to the specified structure.

## Success Criteria

1. The API is accessible and returns a success status code (200 OK, 204 No Content) for assigning a teacher to a course.
2. Assigning a teacher results in the correct course record being updated with a valid teacher ID.
3. Retrieving a course's information successfully returns a JSON object with complete details, including the teacher's information.
4. Attempting to assign a non-existent teacher returns an appropriate error response with a relevant status code (400 Bad Request).
5. The database schema successfully integrates the new `teacher_id` field in the Course entity while preserving the existing data integrity of Students and Courses.

## Key Entities

- **Course Entity** (Updated):
  - `id`: Integer (automatically generated identifier for each Course)
  - `name`: String (required name of the Course)
  - `level`: String (required level of the Course)
  - `teacher_id`: Integer (optional, ID of the assigned Teacher)

- **Teacher Entity** (Existing):
  - `id`: Integer (automatically generated identifier for each Teacher)
  - `name`: String (required name of the Teacher)
  - `email`: String (required email of the Teacher)

- **Student Entity** (Existing):
  - `id`: Integer (automatically generated identifier for each Student)

## Assumptions

1. Users have the necessary permissions to assign teachers to courses within the application.
2. The application will validate that the `teacher_id` field corresponds to an existing Teacher entity.
3. The database migration will be thoroughly tested to ensure existing data for Students, Courses, and Teachers remains intact.

## Out of Scope

1. User interface development for Course and Teacher assignment; the specification focuses solely on API endpoints and database updates.
2. Advanced features enabling multiple teacher assignments or bulk assignments for courses are not included and may be addressed in future iterations.
3. User authentication and authorization for API endpoint security around Course and Teacher management are outside this scope.
4. Notification systems or email functionalities for course assignment events are not part of the current feature.