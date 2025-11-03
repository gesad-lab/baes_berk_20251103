# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities, enabling students to be associated with one or more courses they are enrolled in. This enhancement will improve the application's ability to manage student course enrollments and facilitate better tracking of student progress.

## User Scenarios & Testing

### User Scenarios
1. **Enroll a Student in a Course**:
   - As an admin, I want to associate a student with a course so that the student's enrollments can be tracked and managed.

2. **Retrieve Student's Courses**:
   - As a user, I want to view the list of courses for a specific student to understand their current enrollments.

3. **Update Course Enrollment for a Student**:
   - As an admin, I want to add or remove courses from a student's enrollment to reflect their current status in the educational program.

### Testing Scenarios
1. Test that a student can be enrolled in a course and that this relationship is saved correctly.
2. Test that retrieving a student retrieves their associated courses accurately.
3. Test that a student's course enrollment can be updated successfully.

## Functional Requirements
1. **Update the Student entity to include a relationship with Course**:
   - Each Student can have multiple associated Course records.

2. **Update the database schema to implement this relationship**:
   - A new table, **StudentCourse**, will be introduced to manage the many-to-many relationship between Students and Courses.
   - **Table Name**: `StudentCourse`
   - **Columns**:
     - `student_id`: Integer (Foreign Key referencing Student.id, required)
     - `course_id`: Integer (Foreign Key referencing Course.id, required)

3. **The application must provide endpoints for managing course enrollments**:
   - **Enroll a Student in a Course**:
     - **Endpoint**: `/students/{student_id}/courses` (POST)
     - **Input**: JSON payload containing `course_id` (Integer, required)
     - **Output**: JSON response confirming enrollment with student_id and course_id.
     
   - **Retrieve Student's Courses**:
     - **Endpoint**: `/students/{student_id}/courses` (GET)
     - **Output**: JSON response with a list of courses for the specified student.

   - **Update Course Enrollment**:
     - **Endpoint**: `/students/{student_id}/courses` (PUT)
     - **Input**: JSON payload containing `course_ids` (Array of Integers, required for updates to reflect current courses)
     - **Output**: JSON response confirming the updated list of courses for the student.

4. **The database migration for adding the StudentCourse table** must ensure that existing Student and Course data remain intact.

## Success Criteria
1. User is able to successfully enroll a student in a course with valid `student_id` and `course_id`, receiving confirmation in the response.
2. User is able to retrieve a list of courses associated with a student, getting accurate enrollment information.
3. User is able to update a student’s list of enrolled courses, with the changes reflected when fetching the student's course list later.
4. The database schema update runs successfully without any disruptions to existing Student or Course data.

## Key Entities
- **StudentCourse Table**:
  - **Columns**:
    - `student_id`: Integer (Foreign Key referencing Student.id, required)
    - `course_id`: Integer (Foreign Key referencing Course.id, required)

## Assumptions
- Admin users have the necessary permissions to associate students with courses.
- There are existing validations in place for student and course IDs to ensure integrity.
- The same tech stack (Python 3.11+ and FastAPI with SQLite) is used as in the previous sprint.
- The integration of Course and Student entities is based on common identifiers (IDs).

## Out of Scope
- Designing user interface components for managing course enrollments.
- Implementing advanced features such as course completion tracking or attendance monitoring.
- Adding additional validation logic for course or student IDs beyond basic existence checks.