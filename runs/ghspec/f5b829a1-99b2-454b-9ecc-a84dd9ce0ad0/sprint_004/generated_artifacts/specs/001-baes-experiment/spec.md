# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the application. This relationship will allow students to be associated with multiple courses, enhancing the capability to manage course enrollment and tracking for students. By implementing this feature, the application will improve usability for educators and administrators, who need to link students with their corresponding courses effectively.

## User Scenarios & Testing
1. **Enroll a Student in a Course**:
   - A user submits a request to enroll a specific student in a specific course.
   - The system confirms the enrollment and returns the details of the student and course.

2. **Retrieve Courses for a Student**:
   - A user requests to retrieve all courses associated with a specific student.
   - The system returns a list of courses that the student is enrolled in.

3. **Handle Invalid Enrollment Input**:
   - A user attempts to enroll a student who does not exist.
   - The system returns an appropriate error response indicating that the student cannot be found.
   - A user attempts to enroll a student in a course that does not exist.
   - The system returns an appropriate error response indicating that the course cannot be found.

### Testing Scenarios
- Test enrolling a student in an existing course.
- Test retrieving courses associated with a student.
- Test enrolling a non-existent student to verify error handling.
- Test enrolling a student in a non-existent course to verify error handling.

## Functional Requirements
1. **Enroll Student in Course**:
   - Endpoint: `POST /students/{studentId}/enroll`
   - Request body: `{ "courseId": "integer" }` (Course ID is required)
   - Response: 201 Created with JSON body `{ "studentId": "integer", "courseId": "integer" }`.

2. **Retrieve Student Courses**:
   - Endpoint: `GET /students/{studentId}/courses`
   - Response: 200 OK with JSON body `{ "courses": [{ "id": "integer", "name": "string", "level": "string" }] }`.
   - Response for non-existing student: 404 Not Found with an error message.

3. **Error Handling**:
   - If the student ID provided does not match any existing student, return 404 Not Found with a message detailing the error.
   - If the course ID provided does not match any existing course, return 404 Not Found with a message detailing the error.

4. **Database Schema Updates**:
   - Update the database schema to establish a many-to-many relationship between the Student and Course entities.
   - Create an enrollment bridge table (such as `student_courses`) to store relationships without losing existing Student and Course data.
   - Ensure that the database migration preserves any existing data in the Student and Course tables.

## Success Criteria (measurable, technology-agnostic)
- Students can be successfully enrolled in courses through a validated API endpoint.
- A student can retrieve a list of all courses they are enrolled in without errors.
- Appropriate error messages are returned when attempting to enroll with invalid student or course IDs.
- All API responses adhere to the specified JSON format.
- The existing Student and Course data remains unchanged and accessible after the schema migration.

## Key Entities
- **Enrollment** (Bridge table between Student and Course):
  - `student_id`: Unique identifier referencing a Student.
  - `course_id`: Unique identifier referencing a Course.

## Assumptions
- Users have suitable permissions to make changes to student enrollments.
- The application is operating within the same overall architecture established in previous sprints.
- Users are familiar with the enrollment process and student-course relationships.

## Out of Scope
- Any functionality related to updating or removing enrollments.
- User authentication or authorization mechanisms.
- Frontend interfaces for managing enrollments (only API endpoints are considered).
- Changes to existing Student or Course entities beyond establishing a relationship.
- Any additional features regarding course management that may not be covered in earlier sprints.