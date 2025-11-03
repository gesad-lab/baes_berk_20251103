# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student entity and the Course entity within the application. By allowing students to be associated with one or more courses, we will support functionalities related to course enrollment, tracking academic progress, and enabling better resource allocation for both students and educators. This integration enhances the application’s ability to manage educational offerings and meets user needs for efficiently tracking student participation in various courses.

## User Scenarios & Testing
1. **User Scenario: Associate Student with Courses**
   - As an administrator, I want to be able to assign courses to students, so that I can keep track of their course enrollments.
   - **Test**: Verify that a PATCH request to the `/students/{id}/courses` endpoint with a list of course IDs successfully associates those courses with the specified student.

2. **User Scenario: Fetch Student Courses**
   - As a user, I want to view all courses associated with a specific student, so that I can monitor their enrollment status.
   - **Test**: Verify that a GET request to the `/students/{id}/courses` endpoint returns a list of course details (e.g., IDs, names, and levels) associated with that student.

3. **User Scenario: Invalid Course Association**
   - As a user, if I attempt to associate a course that does not exist with a student, I want to receive a clear error message explaining the issue.
   - **Test**: Verify that a PATCH request with an invalid course ID returns a 404 error status and an appropriate error message.

## Functional Requirements
1. **Associate Courses with Student**
   - Endpoint: `PATCH /students/{id}/courses`
   - Request Body:
     - `course_ids`: array of integers (course IDs), required
   - Response:
     - 200 OK with a JSON message confirming the courses have been successfully associated with the student.

2. **Fetch Associated Courses for Student**
   - Endpoint: `GET /students/{id}/courses`
   - Response:
     - 200 OK with a JSON array containing objects for each associated course, including `id`, `name`, and `level`.

3. **Error Handling for Course Association**
   - If the request includes an invalid course ID:
     - 404 Not Found and a JSON error message stating "Course not found."

4. **Database Schema Update**
   - The existing database schema must be updated to create a many-to-many relationship between Students and Courses:
     - A new join table called `student_courses` with the following fields:
       - `student_id`: integer, foreign key referencing `Student(id)`.
       - `course_id`: integer, foreign key referencing `Course(id)`.
   - A database migration must be created to incorporate this new join table while preserving existing Student and Course data.

## Success Criteria
- The application can successfully associate courses with students and retrieve those associations without errors.
- The application returns appropriate success and error messages in JSON format.
- Cover at least 70% of business logic with automated tests, particularly for endpoints handling course associations and retrieval.
- Ensure that the database migration does not result in data loss, preserving existing Student and Course records and relationships.

## Key Entities
- **Student**
  - Attributes:
    - `id` (integer, primary key, auto-increment)
    - Existing attributes remain unchanged.

- **Course**
  - Attributes:
    - `id` (integer, primary key, auto-increment)
    - Existing attributes remain unchanged.

- **StudentCourses** (Join Table)
  - Attributes:
    - `student_id` (integer, foreign key referencing `Student(id)`)
    - `course_id` (integer, foreign key referencing `Course(id)`)

## Assumptions
- It is assumed that student IDs and course IDs provided in requests correspond to existing records in the database.
- The system can handle multiple associations between students and courses without performance degradation.
- Users accessing this feature have proper authorization to modify course associations for students.

## Out of Scope
- Any changes or features related to course management, such as creating or deleting courses, are outside the scope of this feature.
- Features related to student grade tracking or attendance monitoring in courses are not included in this specification.