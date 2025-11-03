# Feature: Add Teacher Relationship to Course Entity

---

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` entity and the `Teacher` entity within the Student Management Web Application. By adding this relationship, we aim to enable better association between courses and their respective teachers. This will facilitate improved course management and provide users with insights into which teacher is responsible for each course, thereby enhancing the overall educational experience.

## User Scenarios & Testing
1. **Assign Teacher to Course**:
   - A user submits a request to assign a teacher to a specific course.
   - The application responds confirming the assignment and provides the updated course details.

2. **Retrieve Course Details with Teacher Info**:
   - A user submits a request to retrieve information about a specific course along with its associated teacher.
   - The application responds with the course information, including the teacher's name and email.

3. **Handle Invalid Teacher Assignment**:
   - A user attempts to assign a teacher to a course where the teacher does not exist.
   - The application responds with an appropriate error message indicating the teacher must be valid.

### Testing
- Verify that assigning a teacher to a course with valid IDs results in a successful response, providing the updated course information.
- Verify that requesting the details of a course returns expected information, including the assigned teacher.
- Verify that attempting to assign a non-existent teacher returns a clear error message indicating the issue.

## Functional Requirements
1. **Assign Teacher to Course API**:
   - Endpoint: `POST /courses/{course_id}/assign_teacher`
   - Request body: `{ "teacher_id": "int" }`
   - Response:
     - Success: `200 OK` with `{ "course_id": "int", "assigned_teacher_id": "int" }`
     - Error: `404 Not Found` if the specified course or teacher does not exist.

2. **Retrieve Course Details API**:
   - Endpoint: `GET /courses/{course_id}`
   - Response:
     - Success: `200 OK` with `{ "course_id": "int", "course_name": "string", "assigned_teacher": { "teacher_id": "int", "name": "string", "email": "string" } }`
     - Error: `404 Not Found` if the specified course does not exist.

3. **Database Schema Changes**:
   - Update the `Course` table to include a foreign key relationship to the `Teacher` entity:
     - Add `teacher_id` (integer, optional) to the `Course` table, referencing the `teacher_id` in the `Teacher` table.
   - Ensure that the existing Student and Course data remain intact during this migration.

## Success Criteria
- The application should successfully assign a teacher to a course when provided a valid `course_id` and `teacher_id`, returning the expected JSON response.
- The application should correctly retrieve and display course details with the assigned teacher's information upon request.
- All API responses must conform to the specified JSON format.
- The database migration process should ensure that existing student and course data is unaffected by the addition of the new relationship.

## Key Entities
- **Course**:
   - Existing attributes:
     - `course_id`: Identifier for the course (integer, primary key).
     - `course_name`: Name of the course (string, required).
   - New attribute:
     - `teacher_id`: Identifier for the assigned teacher (integer, foreign key, optional).

- **Teacher**:
   - Existing attributes as defined in the previous sprint.

## Assumptions
- Users submitting requests to assign teachers will provide valid `course_id` and `teacher_id` inputs.
- The application should validate the existence of the teacher being assigned to ensure data integrity.
- Database migrations can be executed without impacting existing functionalities related to `Student` and `Course`.

## Out of Scope
- Unassignment of teachers from courses or management thereof.
- Any additional functionality related to teacher evaluations or course feedback.
- Modifications to the `Teacher` entity beyond what is specified for the relationship.
- Updates or deletions of course records associated with the teacher.

---