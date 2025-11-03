# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course and Teacher entities within the existing system. By allowing each Course to be associated with a Teacher, we enhance the application's capability to manage course assignments more effectively, which aids in tracking instructional resources and improving reporting functionality.

## User Scenarios & Testing
1. **Associating a Teacher with a Course**: A user sends a request to associate a specific teacher with a course by providing the course ID and teacher ID. The system should successfully link the two entities and return the course details, including the teacher information.

2. **Retrieving Course with Teacher Details**: A user sends a request to retrieve course details. The system should return the course information along with the associated teacher's name and email.

3. **Updating Teacher for a Course**: A user sends a request to update the teacher assigned to a course by providing the course ID and new teacher ID. The system should successfully update the relationship and return the updated course details.

4. **Error Handling for Invalid Associations**: The system must validate that the provided teacher ID exists and is valid for a given course, returning appropriate error messages if the validation fails.

5. **Database Migration Verification**: After the database schema update, a user should verify that the relationship between Courses and Teachers is established without affecting existing Student or Course data, ensuring full data integrity.

## Functional Requirements
1. Update the Course entity to include a new relationship field:
   - **Teacher ID**: A foreign key reference to the `Teacher` entity, allowing a course to have one associated teacher. This field should be nullable to maintain backward compatibility.

2. Implement the following API functionality for managing course-teacher associations:
   - Associate a teacher with a course: `POST /courses/{courseId}/assignTeacher` (requiring `teacherId`).
   - Retrieve course details with associated teacher information: `GET /courses/{courseId}`.
   - Update the teacher for a specific course: `PUT /courses/{courseId}/assignTeacher` (requiring updated `teacherId`).

3. The application must implement a database migration that:
   - Updates the existing `course` table to include a new `teacher_id` field as a foreign key referencing the `teacher` table.
   - Ensures that existing Course and Teacher data remain intact while preserving data integrity and associations.

4. The API responses must remain in JSON format for both success and error scenarios, ensuring consistent formatting for operations related to course-management activities.

## Success Criteria
- Successfully assigning a teacher to a course should return a 200 OK status with updated course details, including teacher information.
- Successfully retrieving course details should return a 200 OK status with course and associated teacher's name and email.
- Successfully updating the teacher assignment should return a 200 OK status with updated course details.
- Validation errors when associating teachers with courses should return a 400 Bad Request status with specific error messages when invalid or missing data is provided.
- The migration process should complete successfully, updating the `course` table without loss of any existing Course data, which can be verified through data integrity checks post-migration.

## Key Entities
- **Course**: Represents an updated course entity with the following additional fields:
  - `teacher_id`: integer (nullable, foreign key referencing `Teacher` entity).

## Assumptions
- The database supports foreign key constraints and migrations necessary for implementing the teacher-course association.
- Existing Course entities within the database will be updated to maintain integrity, with `teacher_id` defaulting to null until actively assigned.
- Users will interact with the application using the existing RESTful API format established in the previous sprint.

## Out of Scope
- User interface changes associated with course-management activities are not included; the focus is on API and database modifications.
- Features related to course scheduling or assigning multiple teachers to a course are excluded from this feature.
- Any modifications to the existing Student entities beyond the context of courses and teachers are not part of this implementation.