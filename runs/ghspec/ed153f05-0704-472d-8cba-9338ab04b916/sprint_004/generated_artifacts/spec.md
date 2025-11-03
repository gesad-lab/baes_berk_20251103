# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within our application. This relationship will enable the association of students with the courses they are enrolled in, thereby enhancing data management and providing better insights into student-course interactions. By allowing students to have multiple courses, we anticipate improved functionality in managing academic progress and course registrations.

## User Scenarios & Testing
1. **Scenario: Associate a Student with a Course**
   - **Given** a student exists and a course exists in the database
   - **When** I send a POST request to the /students/{id}/courses endpoint with the course ID
   - **Then** the student should be successfully associated with the course, and I should receive a success response confirming the enrollment.

2. **Scenario: Retrieve All Courses for a Student**
   - **Given** a student is associated with multiple courses
   - **When** I send a GET request to the /students/{id}/courses endpoint
   - **Then** I should receive a JSON response listing all courses associated with the student, including course IDs, names, and levels.

3. **Scenario: Validation of Course Enrollment**
   - **Given** a student does not exist in the database
   - **When** I send a POST request to enroll the student in a course
   - **Then** I should receive an error response indicating that the student does not exist.

## Functional Requirements
1. **Course Relationship Addition**:
   - Define a many-to-many relationship between the Student and Course entities, whereby a student can be enrolled in multiple courses and a course can have multiple students.

2. **API Endpoints**:
   - **POST /students/{id}/courses**: Enroll a student in a course.
     - Request Body: `{ "course_id": "number" }`
     - Response: `{ "message": "Enrollment successful." }` (Status Code: 201 Created)
   - **GET /students/{id}/courses**: Retrieve a list of courses for a specific student.
     - Response: `[{ "id": "number", "name": "string", "level": "string" }, ...]` (Status Code: 200 OK)

3. **Database Schema Update**:
   - Update the database schema to create a join table (e.g., `student_courses`) that links the Student and Course tables.
   - The join table should reference the `student_id` and `course_id`, ensuring that existing data in the Student and Course tables remains intact during the migration.

## Success Criteria
- The application starts up without errors and updates the database schema to include a new `student_courses` join table.
- Successful enrollment of a student in a course returns a status code of 201 Created with a confirmation message.
- Retrieving all courses for a student returns the correct list of courses with each course's ID, name, and level, along with a status code of 200 OK.
- Proper error handling for non-existent students during course enrollment returns a status code of 404 Not Found with a clear message.

## Key Entities
- **StudentCourse** (Join Entity):
  - `student_id`: Integer (foreign key referencing Student)
  - `course_id`: Integer (foreign key referencing Course)

## Assumptions
- Students and courses are uniquely identified by their IDs within the application.
- The system allows authenticated users to enroll students in courses via the API.
- The existing database structure can accommodate the addition of the join table without losing existing data.
- Valid course IDs provided in requests will correspond to existing courses.

## Out of Scope
- Any user interface modifications or enhancements related to displaying student course enrollments are not included in this specification.
- Features for managing course un-enrollment or additional restrictions based on course capacity are not part of this feature.
- Detailed validation on course IDs beyond checking for existence in the Course table is not included.
- Reporting on student performance or statistics tied to course enrollments is outside the scope of this implementation.