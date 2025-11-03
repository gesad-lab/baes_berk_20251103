# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student entity and the newly created Course entity. By enabling students to have associated courses, we can enhance the educational data structure of the application, facilitate course enrollments, and improve user experience in managing student-course connections.

## User Scenarios & Testing
1. **Associate Students with Courses**: As a school administrator, I want to be able to assign courses to students so that I can track the courses each student is enrolled in.
   - *Test*: Update a student's record with a course ID and verify that the course is successfully associated with the student in the database.

2. **Retrieve Student Courses**: As a user, I want to retrieve a student's list of enrolled courses so that I can see the courses they are taking.
   - *Test*: Query a student’s record and check that the associated courses are accurately returned in the response.

3. **Handle Association Errors**: As a school administrator, I want to be informed if I attempt to associate a course with a student that does not exist or if the course ID is invalid.
   - *Test*: Try to associate a student with a nonexistent course ID and verify that an appropriate error message is returned.

## Functional Requirements
1. **Associate Courses with a Student**:
   - Method: PATCH
   - Endpoint: `/students/{student_id}/courses`
   - Request Body:
     - JSON object with:
       - `course_id` (integer, required)
   - Response:
     - 200 OK on successful association of the course with the student
     - 400 Bad Request for validation errors (e.g., invalid course ID)

2. **Retrieve Student Courses Endpoint**:
   - Method: GET
   - Endpoint: `/students/{student_id}/courses`
   - Response:
     - 200 OK with a JSON array of course objects associated with the requested student.

3. **Database Schema Management**:
   - Update the existing Student table to include a relationship with the Course table:
     - Table: `Student`
       - Add a new field `course_ids`: Array of Integers (list of course IDs)
   - Ensure that the database migration preserves existing data for both students and courses while establishing the new relationship.

## Success Criteria
1. The application should allow the association of a course to a student and return a success response confirming the relationship.
2. The application should allow retrieval of a list of courses that a student is enrolled in, accurately reflecting the associations made.
3. The application should validate the existence of the input course ID and handle errors gracefully by returning appropriate messages for any association issues (e.g., nonexistent course).

## Key Entities
- **Student**:
  - Existing Attributes:
    - `id`: Integer, Unique Identifier
    - `name`: String, Required Field
    - `course_ids`: Array of Integers (list of associated course IDs)

- **Course**:
  - Attributes:
    - `id`: Integer, Unique Identifier
    - `name`: String, Required Field
    - `level`: String, Required Field

## Assumptions
- The application environment supports the modification of the existing Student table to incorporate the new course relationship accurately.
- Users will provide valid course IDs that exist in the Course table while associating them with students.
- The database migration will safely apply the new relationship changes without data loss or disruption.

## Out of Scope
- User authentication and authorization for accessing course association endpoints.
- Any reporting or analytics features related to student-course enrollments.
- Detailed course management features such as tracking grades or attendance within this sprint.