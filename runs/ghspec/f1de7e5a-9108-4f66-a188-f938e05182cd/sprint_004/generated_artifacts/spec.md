# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to introduce a relationship between the `Student` entity and the newly created `Course` entity within our existing system. By establishing this connection, students will be able to enroll in various courses, enhancing their learning experience and enabling better management of course registrations. This integration is essential for providing a comprehensive view of students' educational engagements.

## User Scenarios & Testing
1. **Link Student to a Course**:
   - As an administrator, I want to associate a student with a course, so that I can track which students are enrolled in which courses.
   - Test: Validate that when an administrator submits a request to link a student to a course, the relationship is created successfully.

2. **Retrieve Courses for a Student**:
   - As a student, I want to see a list of courses I am enrolled in, so that I can manage my educational commitments better.
   - Test: Validate that a GET request for student information includes an array of courses with relevant details.

3. **Enforcement of Course Enrollment Rules**:
   - As a user, I want to receive an error message if I attempt to enroll a student in a course that does not exist.
   - Test: Validate that an appropriate error message is returned when attempting to associate a student with a non-existent course.

## Functional Requirements
1. The application must provide an updated API endpoint to associate a student with a course:
   - **Endpoint**: `/students/{student_id}/enroll` (POST)
   - **Request Body**:
     ```json
     {
         "course_id": "<integer>"
     }
     ```
   - **Response**:
     - Status code 201 (Created) indicating the student has been successfully enrolled in the course.

2. The application must provide an updated API endpoint to retrieve the courses linked to a student:
   - **Endpoint**: `/students/{student_id}/courses` (GET)
   - **Response**:
     - Status code 200 (OK) with a JSON array of course objects that the student is enrolled in.

3. The application must validate the input data:
   - The `course_id` must correspond to an existing course.
   - The application must return a status code 400 (Bad Request) if the `course_id` does not reference a valid course.

4. The SQLite database schema must be updated to include a new junction table to support the many-to-many relationship between `Student` and `Course` entities:
   - **Table Name**: `student_courses`
   - **Fields**:
     - `student_id`: Integer (foreign key referencing `Student`)
     - `course_id`: Integer (foreign key referencing `Course`)
     - Primary Key: Composite key on both `student_id` and `course_id`

5. A database migration must be created to add the `student_courses` junction table while preserving existing `Student` and `Course` data.

## Success Criteria
1. Users can successfully enroll a student in a course by submitting a valid request, receiving a 201 status code with confirmation.
2. Users can retrieve a list of courses enrolled by a specific student, with a response that includes valid JSON data of the courses.
3. Input validation works effectively, returning a 400 status code when an invalid `course_id` is provided, along with a descriptive error message.
4. The application initializes without errors, and the SQLite database accurately reflects the new schema, maintaining existing `Student` and `Course` data integrity.

## Key Entities
- **StudentCourses**:
  - Attributes:
    - `student_id`: Integer (foreign key referencing `Student`)
    - `course_id`: Integer (foreign key referencing `Course`)
    - Primary Key: Composite key of (`student_id`, `course_id`)

## Assumptions
- The web application continues to operate in an environment utilizing SQLite for data persistence.
- Data integrity will be monitored with appropriate foreign key constraints in the database schema.
- Administrators have the necessary permissions to enroll students in courses.

## Out of Scope
- The UI changes necessary for administrators to link students with courses directly are not included in this feature, as the focus is solely on back-end API functionality.
- Complex business logic regarding course prerequisites or limits on enrollments will not be covered in this iteration.
- Real-time notifications to students about their enrollments or course updates are not within the scope of this feature.