# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` and the newly created `Teacher` entities. By allowing each course to be associated with a specific teacher, the application enhances the overall functionality of course management, thereby improving the educational experience and resource allocation within educational institutions. This feature builds upon previous enhancements made in Sprint 5, particularly the creation of the `Teacher` entity, ensuring that the system efficiently manages associations between courses and their respective teachers.

## User Scenarios & Testing
1. **Assign a Teacher to a Course**:
   - A user submits a request to update an existing course to assign a teacher to it.
   - The system confirms the course update and returns the course details including the newly assigned teacher.

2. **Handle Invalid Teacher Assignments**:
   - A user attempts to assign a non-existent teacher to a course.
   - The system returns an appropriate error response indicating that the teacher does not exist.

3. **Unassign a Teacher from a Course**:
   - A user submits a request to remove a teacher from a course.
   - The system confirms the course update removing the association with the teacher.

### Testing Scenarios
- Test assigning a valid teacher to an existing course and verify the update is reflected in the course details.
- Test attempting to assign an invalid (non-existent) teacher to ensure proper error handling.
- Test removing a teacher from a course and verify the course data reflects this change.
- Ensure that existing Student and Course data remain intact after the relationship is added.

## Functional Requirements
1. **Assign Teacher to Course**:
   - Endpoint: `PUT /courses/{course_id}/assign-teacher`
   - Request body: `{ "teacher_id": "integer" }` (Teacher ID must correspond to an existing teacher)
   - Response: 200 OK with JSON body `{ "id": "integer", "name": "string", "teacher_id": "integer" }`.

2. **Error Handling**:
   - If the specified teacher ID does not exist, return 404 Not Found with a message stating that the teacher does not exist.
   - Validate that a course exists before attempting to assign a teacher; return 404 Not Found if the course does not exist.

3. **Remove Teacher from Course**:
   - Endpoint: `DELETE /courses/{course_id}/unassign-teacher`
   - Response: 200 OK with JSON body `{ "id": "integer", "message": "Teacher unassigned successfully" }`.

4. **Database Schema Updates**:
   - Update the `Course` table to include a foreign key reference to the `Teacher` table:
     - `teacher_id`: Foreign key linked to the `Teacher` entity.
   - Ensure that the database migration preserves existing Student, Course, and Teacher data without data loss.

## Success Criteria (measurable, technology-agnostic)
- Teachers can be successfully assigned to courses through a validated API endpoint.
- A JSON response is returned upon successful assignment or unassignment of a teacher containing the relevant course details.
- Appropriate error messages are returned when attempting to assign a non-existent teacher or an invalid course.
- Existing Student and Course data remains unchanged and accessible after the schema update.

## Key Entities
- **Course**:
  - `id`: Unique identifier for the course.
  - `name`: The name of the course (string).
  - `teacher_id`: Foreign key referencing the assigned teacher's ID (integer).
  
- **Teacher** (unchanged):
  - `id`: Unique identifier for the teacher.
  - `name`: Name of the teacher (string, required).
  - `email`: Email of the teacher (string, required).

## Assumptions
- Users have suitable permissions to assign or unassign teachers to/from courses.
- The application continues to follow the same architecture established in previous sprints.
- Users are familiar with how to manage course-teacher relationships.

## Out of Scope
- Any functionality related to creating, updating, or deleting courses beyond adding/removing teacher assignments.
- User authentication or authorization mechanisms.
- Frontend interfaces for managing course-teacher relationships (only API endpoints are considered).
- Additional features related to the Course or Teacher management that may not be covered in earlier sprints.

---

This specification outlines the integration of a teacher relationship into existing Course entities, building upon the previous feature regarding teacher entity creation while ensuring that existing systems and data are preserved.