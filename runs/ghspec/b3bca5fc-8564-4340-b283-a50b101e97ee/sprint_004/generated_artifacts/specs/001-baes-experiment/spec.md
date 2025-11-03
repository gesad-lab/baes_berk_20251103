# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing Student and Course entities in our database. This relationship will enable students to enroll in one or more courses, enhancing the functionality of our educational platform and allowing for more comprehensive management of student data related to their course enrollments. 

## User Scenarios & Testing
### User Scenarios
1. **Enrolling Students in Courses**:
   - As a user, I want to enroll a Student in a Course so that I can effectively manage their academic progress.

2. **Retrieving Student Course Enrollment**:
   - As a user, I want to retrieve a list of Courses a Student is enrolled in to monitor their academic involvement.

3. **Error Handling**:
   - As a user, I want to be informed if I attempt to enroll a Student in a Course that does not exist.

### Testing
1. Test the enrollment of a Student in a valid Course.
2. Test the response when trying to enroll a Student in a non-existent Course.
3. Test the retrieval of enrolled Courses for a Student to ensure the correct list is returned.

## Functional Requirements
1. **Enroll Student in Course**:
   - Endpoint: POST `/students/{student_id}/enroll`.
   - Input: A JSON object containing the `course_id` (string) of the Course to enroll the Student in.
   - Output: A JSON response confirming the Student's enrollment in the Course, including their Student ID and Course ID.

2. **Retrieve Student's Enrolled Courses**:
   - Endpoint: GET `/students/{student_id}/courses`.
   - Output: A JSON array containing all Courses the Student is enrolled in, including course details like `id`, `name`, and `level`.

3. **Database Schema Update**:
   - On application startup, the database schema must be updated to include a new junction table called `student_courses` that references the `Student` and `Course` tables. The table should have the following columns:
     - `student_id`: Foreign key referencing the Student entity (non-null).
     - `course_id`: Foreign key referencing the Course entity (non-null).
   - The migration process should ensure that existing Student and Course data remains intact and correctly associated post-migration.

## Success Criteria (measurable, technology-agnostic)
1. The application must respond with a 201 status code and a confirmation message including Student ID and Course ID upon successful enrollment.
2. The application must respond with a 200 status code and a JSON array of Course details when retrieving a Student's enrolled Courses.
3. The application should validate input and respond with a 400 status code and an appropriate error message when an invalid enrollment request (e.g., non-existent course) is made.
4. The database must be updated on startup with the new schema reflecting the `student_courses` table, without affecting existing Student or Course data.

## Key Entities
- **Student**:
  - Existing entity; ensure no changes made to it.
- **Course**:
  - Existing entity; ensure no changes made to it.
- **StudentCourses** (junction table):
  - Fields:
    - `student_id`: Foreign key referencing the Student entity.
    - `course_id`: Foreign key referencing the Course entity.

## Assumptions
- Users are expected to already have Student and Course entries in the system.
- The application will utilize a consistent development environment as per the previous sprint, similar to an educational database setup.
- The functionality will be used by users familiar with API interactions, such as Postman.

## Out of Scope
- User interface for managing course enrollments; the focus is on the backend API.
- Additional features, such as managing enrollment statuses or prerequisites for Courses.
- The ability to unenroll Students from Courses within this feature directive; will require separate specifications.