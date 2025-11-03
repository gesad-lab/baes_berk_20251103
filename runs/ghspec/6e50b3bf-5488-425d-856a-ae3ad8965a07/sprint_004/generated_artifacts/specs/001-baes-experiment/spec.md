# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing `Student` and `Course` entities in the Student Management Web Application. This relationship will enable each student to be associated with one or more courses, thus facilitating better tracking of student enrollments and improving the overall management of educational offerings. By implementing this feature, we aim to enhance stakeholders' visibility into students' course enrollments and provide an enriched user experience.

## User Scenarios & Testing
1. **Enroll Student in Course**:
   - A user submits a request to enroll a student in a specific course.
   - The application responds with the details of the updated student record, including the associated courses.

2. **Retrieve Student Courses**:
   - A user submits a request to retrieve all courses associated with a particular student.
   - The application responds with a list of courses the student is enrolled in.

3. **Student Without Courses Handling**:
   - A user attempts to retrieve courses for a student who is not enrolled in any courses.
   - The application responds with an appropriate message indicating no courses are associated with that student.

### Testing
- Verify that enrolling a student in a course updates the student record successfully and returns the expected response, including the associated course(s).
- Verify that retrieving a student's courses returns the correct list of courses and their details.
- Verify that querying a student without course enrollments returns a response indicating no courses are found.

## Functional Requirements
1. **Enroll Student in Course API**:
   - Endpoint: `POST /students/{student_id}/courses`
   - Request body: `{ "course_id": "int" }`
   - Response:
     - Success: `200 OK` with `{ "student_id": "int", "courses": [...] }`
     - Error: `404 Not Found` if the specified student or course does not exist.

2. **Retrieve Student Courses API**:
   - Endpoint: `GET /students/{student_id}/courses`
   - Response:
     - Success: `200 OK` with `{ "student_id": "int", "courses": [...] }`
     - Error: `404 Not Found` if the student does not exist.

3. **Database Schema**:
   - Update the `Student` table to include a new relationship with the `Course` entity:
     - Introduce a new table `Student_Course` with the following columns:
       - `student_id` (integer, foreign key referencing `Student`).
       - `course_id` (integer, foreign key referencing `Course`).
       - This table will represent the many-to-many relationship allowing multiple courses for each student.
   - Ensure that the database migration process preserves existing `Student` and `Course` data.

## Success Criteria
- The application should successfully enroll students in courses, providing the expected JSON response.
- The application should return the correct list of courses for a student upon retrieval.
- All API responses must conform to the specified JSON format.
- Existing student and course data should remain intact during the database schema update.

## Key Entities
- **Student_Course**: 
   - Attributes:
     - `student_id`: Identifier for the student (integer, foreign key).
     - `course_id`: Identifier for the course (integer, foreign key).

## Assumptions
- Users will provide valid student and course IDs when enrolling in a course.
- The application can perform database migrations without impacting existing `Student` and `Course` entity functionalities.
- Input validation will ensure that students and courses exist before processing enrollments.

## Out of Scope
- Changes to the existing `Student` and `Course` entity definitions beyond establishing the relationship.
- Functionality for managing course details or content, including course creation or updates.
- User permissions or roles affecting who can enroll students in courses.