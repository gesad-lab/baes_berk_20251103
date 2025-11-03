# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity within the existing educational system. This relationship allows each course to be attributed to a specific teacher, improving the tracking of course ownership and accountability. By implementing this feature, the system aims to enhance the educational experience by clearly defining which teacher is responsible for each course, thereby supporting better administrative management and resource allocation.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**: An admin user wants to assign a teacher to a specific course.
   - **Test Cases**:
     - Successfully assigning a valid teacher ID to a course should update the course record in the database to reflect the teacher’s association.
     - Attempting to assign an invalid teacher ID (non-existent) should return a validation error message indicating that the teacher does not exist.
     - Assigning a teacher to a course that already has an assigned teacher should update the existing relationship correctly without losing the previous assignment.

2. **Retrieving Course Information with Teacher Details**: A user wants to view the details of a specific course, including the assigned teacher.
   - **Test Cases**:
     - Requesting course information with a valid course ID should return details of the course, including the teacher’s name and email.
     - Requesting information with an invalid course ID should return a relevant error message indicating that the course does not exist.

## Functional Requirements
1. **Course-Teacher Relationship**:
   - Update the Course entity to include a relation to the Teacher entity, allowing each course to have one assigned teacher.
   - The relationship should be optional, meaning a course may not necessarily have a teacher assigned initially.

2. **Database Schema Update**:
   - Modify the existing Course table in the database schema to add a foreign key reference to the Teacher entity.
   - Ensure that existing data related to Students, Courses, and Teachers is preserved during the migration process and that the relationship supports null values (i.e., a course can exist without a teacher).

3. **API Endpoints**:
   - `PUT /courses/{course_id}/assign-teacher`: Assign a teacher to a course.
     - Request body: JSON containing the teacher_id.
     - Response: Confirms that the teacher has been successfully assigned to the course along with the updated course details.
   - `GET /courses/{course_id}`: Retrieve course information including assigned teacher.
     - Response: Returns course details in JSON format including teacher information if available.

4. **JSON Responses**: All API responses must conform to JSON format, ensuring that the fields for course and teacher relationships are included.

## Success Criteria
- Successfully assigning a teacher to a course using the `PUT /courses/{course_id}/assign-teacher` endpoint must return a 200 status code and the updated course details.
- The `GET /courses/{course_id}` endpoint must return a 200 status code and display valid course information, including the teacher's details, or a 404 status code if the course does not exist.
- Validation must ensure that appropriate error messages are returned for any invalid teacher IDs or if there are attempts to assign a teacher where the course doesn't exist.

## Key Entities
- **Course**:
  - `id`: (integer, auto-incremented primary key)
  - `name`: (string, required)
  - `level`: (string, required)
  - `teacher_id`: (integer, optional reference to Teacher entity)

- **Teacher** (existing)
  - `id`: (integer, auto-incremented primary key)
  - `name`: (string, required)
  - `email`: (string, required, must be unique if applicable)

- **Student** (existing)
  - `id`: (integer, auto-incremented primary key)
  - `name`: (string, required)
  - `courses`: (list of course IDs associated with the student)

## Assumptions
- The current system is designed to allow for schema modifications without data loss and is capable of handling new relationships.
- Admin users are responsible for managing course assignments and have the necessary permissions for teacher associations.
- The teacher ID provided during the assignment process must refer to an existing teacher in the database.

## Out of Scope
- User interface components for assigning teachers to courses.
- Advanced functionalities such as bulk assignments of teachers, teacher removal, or advanced course management features.
- Authentication and authorization aspects for managing course-teacher relationships, which will be addressed in future iterations.
- Comprehensive reporting or analytics regarding course assignments and teacher performance are not included in this specification.