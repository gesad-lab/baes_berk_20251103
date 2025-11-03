# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` entity and the newly created `Teacher` entity within the educational management system. By enabling each course to have a designated teacher, this feature will enhance the system's ability to manage course assignments, facilitate better communication between teachers and students, and streamline administrative functions. This relationship is crucial for improving the educational experience and ensuring organizational efficiency.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**:
   - A user submits a request to assign a teacher to a specific course.
   - The application processes the request and updates the course with the teacher's information, returning the updated course details.

2. **Retrieving a Course with Assigned Teacher**:
   - A user requests to see the details of a specific course, including its assigned teacher.
   - The application returns the course's information, including the teacher's name and contact details.

3. **Handling Invalid Teacher Assignments**:
   - A user attempts to assign a teacher who does not exist in the `Teacher` entity to a course.
   - The application returns a clear error message indicating that the specified teacher is invalid.

4. **Unassigning a Teacher from a Course**:
   - A user submits a request to unassign a teacher from a course.
   - The application processes the request and updates the course to remove the teacher, returning the updated course details.

**Testing**: Each user scenario will be validated with automated tests to ensure that the relationship functionality operates as expected.

## Functional Requirements
1. **Assign Teacher to Course**:
   - Endpoint: POST `/courses/{course_id}/assign_teacher`
   - Request Body: `{ "teacher_id": "int" }` (teacher_id is required)
   - Response: 200 OK with JSON of the updated course's details.

2. **Retrieve Course with Assigned Teacher**:
   - Endpoint: GET `/courses/{course_id}`
   - Response: 200 OK with JSON of the course's details including assigned teacher: `{ "id": "int", "name": "string", "teacher": { "id": "int", "name": "string", "email": "string" } }`.

3. **Handle Invalid Teacher Assignments**:
   - Validate that the specified teacher_id exists in the system.
   - Response: 400 Bad Request with an error message if the teacher_id is invalid.

4. **Unassign Teacher from Course**:
   - Endpoint: DELETE `/courses/{course_id}/unassign_teacher`
   - Response: 200 OK with JSON of the updated course's details post unassignment.

5. **Database Changes**:
   - Update the database schema for the `Course` table to include a `teacher_id` field:
     - **courses** table:
       - `teacher_id`: Integer (Foreign Key referencing Teacher's id, nullable)
   - Ensure the migration script adds the new `teacher_id` field without affecting existing Student, Course, and Teacher data.

## Success Criteria
- The application must successfully allow users to assign and unassign teachers to/from courses, with valid JSON responses.
- All API endpoints must respond with appropriate HTTP status codes and handle error situations effectively.
- Maintain a minimum test coverage of 70% for business logic related to course-teacher relationships.
- The database schema must be updated correctly with the addition of the `teacher_id` field in the `courses` table, ensuring that existing data remains intact.

## Key Entities
- **Course**:
  - Attributes:
    - `id`: Integer (Primary Key)
    - `name`: String (required)
    - `teacher_id`: Integer (Foreign Key referencing `Teacher`, nullable)

- **Teacher**:
  - Attributes:
    - `id`: Integer (Primary Key)
    - `name`: String (required)
    - `email`: String (required, unique)

## Assumptions
- Users have a fundamental understanding of how to make API requests to assign and manage teachers in courses.
- The teacher_id provided during assignment must correspond to an existing teacher; otherwise, an error will be returned.
- Existing course data does not need to be altered aside from adding the teacher_id attribute.

## Out of Scope
- User interface changes related to assigning or unassigning teachers from courses. This feature will focus solely on backend API functionalities.
- Detailed reporting capabilities or analytics involving teacher-student ratios within courses will not be included in this iteration.
- Additional attributes or features for courses beyond the teacher assignment (e.g., scheduling, enrollment caps) will not be considered in this development cycle.

### Reference to Previous Sprint
- Ensure the integration of the course-teacher relationship utilizes the `Teacher` entity and adheres to the previous sprint specifications regarding the existing `Course` and `Teacher` models.