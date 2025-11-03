# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the student management system. This addition will allow students to enroll in multiple courses, thereby providing a more comprehensive and organized method for managing student enrollments in academic offerings. This feature builds upon the previously implemented Course entity and maintains the existing functionalities of the system while enhancing the academic management capabilities for administrators.

## User Scenarios & Testing
1. **User Story 1: Enroll a Student in a Course**
   - As an admin, I want to enroll a student in a specific course by providing the student ID and course ID, so that I can manage student enrollments effectively.
   - **Testing**: Verify that a POST request to the `/students/{id}/enroll` endpoint with a valid course ID successfully enrolls the student in the course and returns a success message.

2. **User Story 2: Retrieve a Student's Courses**
   - As an admin, I want to view all courses a specific student is enrolled in by providing the student ID, so that I can ensure accurate records of student enrollments are maintained.
   - **Testing**: Verify that a GET request to the `/students/{id}/courses` endpoint returns a list of courses including their IDs, names, and levels for the student.

3. **User Story 3: Error Handling for Invalid Enrollment**
   - As a user, I want to receive informative error messages when I attempt to enroll a student in a course with a non-existing student or course ID, as both must be valid.
   - **Testing**: Verify that a POST request to the `/students/{id}/enroll` endpoint with an invalid student or course ID results in a 400 Bad Request status and an error message indicating the issue.

## Functional Requirements
1. **Enroll Student in Course**:
   - Endpoint: `POST /students/{id}/enroll`
   - Request Body: 
     ```json
     {
       "course_id": "integer"  // required
     }
     ```
   - Response: 
     ```json
     {
       "message": "Student enrolled successfully in the course."
     }
     ```

2. **Retrieve Student's Courses**:
   - Endpoint: `GET /students/{id}/courses`
   - Response:
     ```json
     {
       "courses": [
         {
           "id": "integer",
           "name": "string",
           "level": "string"
         }
       ]
     }
     ```
   - Error Response for non-existing student ID:
     ```json
     {
       "error": {
         "code": "E404",
         "message": "Student not found."
       }
     }
     ```

3. **Validation**:
   - Ensure `course_id` is required and valid.
   - Return a 400 Bad Request status with a specific message if validation fails.

4. **Database Initialization**:
   - Update the database schema to:
     - Establish a many-to-many relationship between Students and Courses.
     - Create an intermediary table (e.g., StudentCourses) with the following fields:
       - `student_id`: integer (foreign key referencing Student)
       - `course_id`: integer (foreign key referencing Course)

5. **Database Migration**:
   - Implement a database migration to create the StudentCourses table while preserving existing Student and Course data.

## Success Criteria
- The application must allow enrolling a student in a course with a valid course ID, returning a success message.
- The application must allow retrieving all courses for a specific student by ID, returning the correct information.
- The application must return appropriate error messages for invalid inputs during enrollment.
- The database schema must be updated to include the StudentCourses table without data loss or corruption of existing Student or Course records.

## Key Entities
- **StudentCourses**
  - `student_id` (integer): A reference to the enrolled student.
  - `course_id` (integer): A reference to the enrolled course.

## Assumptions
- Users of the application have the necessary permissions to enroll students in courses.
- The application will support regular integer inputs for student and course IDs.
- The StudentCourses intermediary table will coexist with existing Student and Course records in the database without interference.

## Out of Scope
- Any additional functionalities related to managing courses beyond enrollment (such as prerequisites, course completion status, etc.).
- User authentication and authorization mechanisms specific to enrollment actions, as the focus is on the API aspect of the application.
- User interface modifications for an enrollment management system beyond what the API supports.

This feature extends the existing system by adding new capabilities while ensuring that current functionalities remain intact and operational. The development should take place in alignment with the structure and principles established in the earlier sprint.