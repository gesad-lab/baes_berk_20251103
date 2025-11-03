# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Student` and `Course` entities within the application. By enabling students to enroll in courses, we enhance the educational management capabilities of the system. This relationship will facilitate tracking which courses each student is enrolled in, thereby improving the user experience for both students and administrators, allowing for a streamlined approach to course administration.

## User Scenarios & Testing
1. **Scenario 1: Enroll a Student in a Course**  
   - **Given**: A student exists in the system.  
   - **When**: An administrator assigns a course to the student.  
   - **Then**: The student's profile should reflect the newly enrolled course, and the course enrollment is stored in the database.

2. **Scenario 2: View Student's Enrolled Courses**  
   - **Given**: A student is already enrolled in one or more courses.  
   - **When**: An administrator requests to view the student's profile.  
   - **Then**: A JSON response should display the student’s details along with a list of enrolled courses.

3. **Scenario 3: Handle Enrollment for Non-Existing Course**  
   - **Given**: An administrator attempts to enroll a student in a course that does not exist.  
   - **When**: The administrator submits the enrollment request.  
   - **Then**: A JSON error response should indicate that the course does not exist.

4. **Scenario 4: Handle Enrollment of Student Already in the Course**  
   - **Given**: A student is already enrolled in a specific course.  
   - **When**: An administrator tries to enroll the student again in the same course.  
   - **Then**: A JSON error response should indicate that the student is already enrolled in this course.

## Functional Requirements
1. **Student-Course Relationship**  
   - Establish a many-to-many relationship between `Student` and `Course` entities:
     - A student can enroll in multiple courses.
     - A course can have multiple students enrolled.

2. **Database Schema Update**  
   - Modify the database schema to include a new join table, `StudentCourses`:
     - Attributes:
       - `id`: Integer (auto-generated ID)
       - `student_id`: Integer (foreign key referencing `Student`)
       - `course_id`: Integer (foreign key referencing `Course`)
     - Ensure that existing `Student` and `Course` data is preserved during migration.

3. **API Endpoints**  
   - **POST /students/{student_id}/enroll**: Accepts a JSON object to enroll a student in a course.
     - Request Body: `{ "course_id": "integer" }`
     - Response: JSON success message indicating enrollment or an error message if the course does not exist or other validation issues occur.
   
   - **GET /students/{student_id}/courses**: Returns a list of courses the student is enrolled in.
     - Response: `[ { "course_id": "integer", "course_name": "string", "course_level": "string" }, ... ]`

4. **Database Migration**  
   - Implement a migration to create the `StudentCourses` join table with the specified fields without affecting existing data in `Student` and `Course`.

5. **JSON Responses**  
   - All API responses must be formatted in JSON, including details of the enrollment or errors.

## Success Criteria
- The application must return a status of 200 OK for successful enrollments and retrieval of enrolled courses, with appropriate error codes for failed requests.
- Enrollment of a student in a course must successfully reflect in the student's data, including a JSON confirmation response that details the enrollment.
- A student can successfully request their list of enrolled courses, which includes displaying course details.
- Attempts to enroll in a non-existent course or a course the student is already enrolled in must return informative error responses.

## Key Entities
- **StudentCourses**
  - Attributes:
    - `id`: Integer (auto-generated ID)
    - `student_id`: Integer (foreign key referencing `Student`)
    - `course_id`: Integer (foreign key referencing `Course`)

## Assumptions
- Users managing student enrollments are familiar with the application's processes for adding and managing student-course relationships.
- The system will validate that both `student_id` and `course_id` are valid before processing enrollments.
- Existing infrastructure will support the addition of a many-to-many relationship without requiring major changes.

## Out of Scope
- User authentication and authorization functionalities surrounding student enrollment processes.
- Implementing features to edit or remove course enrollments for students.
- Any adjustments to the front-end beyond the outlined API endpoints.
- Handling other relationships or dependencies that do not directly involve the `Student` and `Course` entities.