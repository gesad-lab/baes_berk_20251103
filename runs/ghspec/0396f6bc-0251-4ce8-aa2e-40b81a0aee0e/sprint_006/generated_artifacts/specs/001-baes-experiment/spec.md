# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a direct relationship between the `Course` entity and the newly created `Teacher` entity. This relationship will allow courses to be assigned to specific teachers, enhancing the information available in the student management application. By linking courses to their respective teachers, the system fosters better management and oversight of educational offerings, promoting improved accountability for teaching assignments.

## User Scenarios & Testing
1. **User Story 1: Assign a Teacher to a Course**
   - As an admin, I want to assign a teacher to a specific course, so that I can ensure each course has an appropriate instructor.
   - **Testing**: Verify that a PATCH request to the `/courses/{courseId}/assign-teacher` endpoint with a valid teacher ID updates the course to reflect the assigned teacher.

2. **User Story 2: Retrieve Course Details with Assigned Teacher**
   - As an admin, I want to view the details of a course, including the teacher assigned to it, so I can manage teaching assignments effectively.
   - **Testing**: Verify that a GET request to the `/courses/{courseId}` endpoint returns course details, including the teacher's name and email.

3. **User Story 3: Error Handling for Invalid Teacher Assignment**
   - As a user, I want to receive informative error messages when I attempt to assign a non-existent teacher to a course, so I can correct my input.
   - **Testing**: Verify that a PATCH request to the `/courses/{courseId}/assign-teacher` endpoint with an invalid teacher ID results in a 404 Not Found status and an error message indicating the issue.

## Functional Requirements
1. **Assign Teacher to Course**:
   - Endpoint: `PATCH /courses/{courseId}/assign-teacher`
   - Request Body: 
     ```json
     {
       "teacherId": "integer" // required
     }
     ```
   - Response: 
     ```json
     {
       "message": "Teacher assigned to course successfully."
     }
     ```

2. **Retrieve Course Details**:
   - Endpoint: `GET /courses/{courseId}`
   - Response:
     ```json
     {
       "course": {
         "id": "integer",
         "title": "string",
         "description": "string",
         "teacher": {
           "id": "integer",
           "name": "string",
           "email": "string"
         }
       }
     }
     ```

3. **Validation**:
   - Ensure `teacherId` is a required field and exists in the `Teacher` table.
   - Return a 404 Not Found status if the `teacherId` provided does not correspond to an existing teacher.
   - Return a 400 Bad Request status if the `courseId` does not correspond to an existing course.

4. **Database Schema Update**:
   - Update the `Course` table to include a new field:
     - `teacher_id`: integer, foreign key referencing `Teacher(id)`.

5. **Database Migration**:
   - Implement a database migration to add the `teacher_id` column to the `Course` table while preserving existing data related to `Students`, `Courses`, and `Teachers`.

## Success Criteria
- The application must allow assigning a teacher to a course, returning a success message.
- The application must allow retrieving course details with the assigned teacher’s information.
- The application must return appropriate error messages for invalid inputs during teacher assignments.
- The database schema must be updated to include the `teacher_id` field on the `Course` table without data loss or corruption of existing records.

## Key Entities
- **Course**
  - `id` (integer): A unique identifier for each course.
  - `title` (string): The title of the course.
  - `description` (string): A brief description of the course.
  - `teacher_id` (integer, foreign key): References the `id` of the assigned teacher.

- **Teacher**
  - Remain unchanged, as defined in the previous sprint.

## Assumptions
- Users of the application have the necessary permissions to assign teachers to courses.
- Teacher IDs will correspond to existing entries in the Teacher table.
- The new `teacher_id` field will coexist with existing data without interfering with current functionalities.

## Out of Scope
- Any additional functionalities related to course scheduling or modifications beyond teacher assignments will be addressed in future sprints.
- User authentication and authorization mechanisms specific to course management actions are not included in this feature specification.
- User interface elements for managing course and teacher relationships beyond what the API supports are not covered.

This feature builds upon the existing system by adding the necessary functionalities to assign teachers to courses, ensuring the management system remains comprehensive and effective. The development will adhere to established practices from earlier sprints to maintain consistent performance and user experience.