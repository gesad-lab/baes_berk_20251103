# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Student` entity and the newly created `Course` entity within the existing student management system. This enhancement aims to enable students to enroll in multiple courses, thereby improving the system's ability to manage student course enrollments and track academic progress over time. By capturing this relationship, the application will facilitate better reporting and analytics on student performance in various courses.

## User Scenarios & Testing
1. **Associating a Course with a Student**:
   - A user sends a request to associate an existing Course with a Student.
   - Outcome: The API returns a success response confirming the association and lists the updated courses for the Student.

2. **Retrieving Student's Courses**:
   - A user retrieves the list of courses that a specific Student is enrolled in by Student ID.
   - Outcome: The API returns the details of the associated courses in a JSON format.

3. **Associating a Non-Existing Course**:
   - A user attempts to associate a Course with a Student, but the Course does not exist.
   - Outcome: The API returns an error response indicating that the specified Course cannot be found.

4. **Validating Database Migration**:
   - The existing database schema is updated to include a reference to the `Course` entity in the `Student` table without losing existing Student data.
   - Outcome: The migration completes successfully, preserving all student records and establishing new associations.

## Functional Requirements
1. The web application must provide an API endpoint to associate a Course with a Student:
   - Endpoint: `POST /students/{student_id}/courses`
   - Input: JSON object that includes the `course_id` (integer).
   - Output: JSON object confirming the association along with the updated list of courses for that Student.

2. The web application must provide an API endpoint to retrieve all courses associated with a Student:
   - Endpoint: `GET /students/{student_id}/courses`
   - Output: JSON object containing an array of courses associated with the specified Student, including course IDs and names.

3. The web application must validate that the `course_id` exists before creating the association:
   - If the `course_id` does not correspond to an existing Course, the application returns an error response.

4. The database schema must be updated to introduce a many-to-many relationship between `Student` and `Course` entities through a junction table (e.g., `student_courses`):
   - The `student_courses` table should have:
     - `student_id`: Integer, foreign key referencing Student entity.
     - `course_id`: Integer, foreign key referencing Course entity.
     - Both fields should form a composite primary key to ensure uniqueness.
   - The update must preserve existing Student and Course data.

## Success Criteria
1. The application must return a successful response (HTTP status 201) when a Course is successfully associated with a Student.
2. The application must return a successful response (HTTP status 200) when retrieving a list of courses for a specific Student.
3. The application must return an error response (HTTP status 404) when attempting to associate a Course that does not exist.
4. The application must successfully apply the database migration, ensuring existing student and course records remain intact and functional.

## Key Entities
- **Student**:
  - Existing entity with attributes related to student information.
  
- **Course**:
  - Existing entity representative of courses available for student enrollment.

- **student_courses** (junction table):
  - `student_id`: Integer, foreign key referencing the Student entity.
  - `course_id`: Integer, foreign key referencing the Course entity.

## Assumptions
- Existing Students and Courses will be maintained without data loss through the migration process.
- Users accessing the application have basic knowledge of using API endpoints and understand data format requirements.
- The application operates in an environment consistent with that of previous sprints.
- JSON responses will adhere to standard formatting practices.

## Out of Scope
- User interface updates regarding the representation of student-course relationships; focus is on backend API and database changes only.
- Additional functionalities related to course prerequisites, enrolment limits, or student permissions beyond basic association.
- Complex validation beyond ensuring existing course associations and maintaining data integrity during migration.