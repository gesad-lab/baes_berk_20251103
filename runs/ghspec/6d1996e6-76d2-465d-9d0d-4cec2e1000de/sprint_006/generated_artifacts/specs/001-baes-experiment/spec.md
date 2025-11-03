# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity within the existing educational system. This will enable each course to be associated with a specific teacher, facilitating better management of course assignments and tracking teaching responsibilities. By implementing this relationship, we enhance the functionality of the system, providing users with comprehensive insights into course management.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**:
   - Given the user has access to the application, when they specify a teacher for an existing course, then the course should successfully reflect that the teacher has been assigned.

2. **Retrieving Course with Teacher Information**:
   - Given the user requests information about a course, when the course has an associated teacher, then the application should return the course details along with the teacher's name in JSON format.

3. **Removing a Teacher from a Course**:
   - Given the user decides to remove a teacher assignment from a course, when they execute the removal, then the application should update the course to reflect that no teacher is assigned.

4. **Handling Errors in Assigning Teachers**:
   - Given a user tries to assign a non-existent teacher to a course, the application should return a clear error message indicating that the teacher does not exist.

## Functional Requirements
1. **Assign Teacher to Course**:
   - Endpoint: PUT /courses/{id}/assign-teacher
   - Request Body: JSON object containing "teacher_id" (integer, required).
   - Response: 200 OK with the updated course object in JSON format, or 404 Not Found if the course ID does not exist.

2. **Retrieve Course with Teacher**:
   - Endpoint: GET /courses/{id}
   - Response: 200 OK with the course object including teacher's name if assigned, or 404 Not Found if the course ID does not exist.

3. **Remove Teacher from Course**:
   - Endpoint: DELETE /courses/{id}/remove-teacher
   - Response: 200 OK with confirmation that the teacher has been removed, or 404 Not Found if the course ID does not exist.

4. **Database Schema Update**:
   - Update the Course table to include a new column:
     - teacher_id: Integer, foreign key referencing the Teacher table (nullable).
   - Ensure migrations preserve existing Student, Course, and Teacher data.

## Success Criteria
- The application must successfully respond to the endpoints related to assigning, retrieving, and removing teachers from courses as specified above.
- The assignment and removal of teachers to and from courses should reflect accurately in the database.
- Proper handling and messaging for error scenarios (such as assigning a non-existent teacher) must be implemented and validated.
- The updated Course table should maintain data integrity and preserve existing records.

## Key Entities
- **Course**:
  - id: Integer, auto-generated primary key.
  - name: String, required.
  - teacher_id: Integer, nullable foreign key referencing Teacher(id).

- **Teacher**:
  - id: Integer, auto-generated primary key.
  - name: String, required.
  - email: String, required.

## Assumptions
- The application will utilize existing validation procedures to ensure that only valid teacher IDs are assigned to courses.
- Users utilizing this feature are familiar with how to use RESTful APIs for managing course and teacher data.
- The application will be deployed in an environment consistent with the current tech stack used in previous sprints.

## Out of Scope
- Modifications to existing features unrelated to the course-teacher relationship, such as course content updates or graphical user interface changes.
- Advanced features, such as scheduling and conflict resolution for courses and teacher assignments; this feature focuses solely on the relationship integration.
- External systems for curriculum management or reporting functionalities; this feature is confined within the current application’s framework.