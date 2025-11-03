# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` entity and the newly introduced `Teacher` entity, allowing each course to be associated with a specific teacher. This relationship enhances the course management capabilities of the application, enabling better tracking of which instructor is responsible for each course and facilitating more effective educational management.

## User Scenarios & Testing
1. **Assign a Teacher to a Course**:
   - **Scenario**: An admin user wants to associate an existing course with a specific teacher.
   - **Test**: Verify that when a valid course ID and teacher ID are provided, the course record is updated with the teacher's information, and the response confirms the successful association.

2. **Error Handling for Invalid Course IDs**:
   - **Scenario**: An admin user attempts to assign a teacher to a course using a non-existent course ID.
   - **Test**: Verify that the system returns a clear error message indicating that the course ID is invalid.

3. **Error Handling for Invalid Teacher IDs**:
   - **Scenario**: An admin user tries to assign a teacher to a course using a non-existent teacher ID.
   - **Test**: Verify that the system prevents the association and returns a clear error message indicating that the teacher ID is invalid.

4. **Database Migration**:
   - **Scenario**: The database schema must be updated to support the relationship between teachers and courses.
   - **Test**: Verify that existing student, course, and teacher data remains intact, and that a new foreign key relationship is established without data loss.

## Functional Requirements
- The application must extend the existing `Course` entity to include a reference to the `Teacher` entity:
  - The `Course` table will include a new attribute:
    - `teacher_id`: integer (foreign key referencing the `Teacher` entity)

- The application must provide an API endpoint to assign a teacher to a course:
  - **PATCH** `/courses/{course_id}`
    - Request Body: Must include a JSON object with `teacher_id` (integer, required).
    - Response: A JSON object confirming the association of the course with the teacher (including updated course details).

- A database migration must be implemented to ensure that existing student, course, and teacher data is preserved during the schema update and that the `teacher_id` foreign key is established on the `Course` table.

- All API responses must be in JSON format.

## Success Criteria (measurable, technology-agnostic)
- The application must allow users to successfully assign a teacher to a course, returning a confirmation response with details of the updated course.
- Users receive a clear error message when trying to assign a teacher using an invalid course ID.
- Users receive a clear error when trying to assign a teacher using an invalid teacher ID.
- The database must contain the `teacher_id` foreign key in the `Course` table upon application startup, without affecting existing student and teacher records.

## Key Entities
- **Course** (existing entity)
  - Attributes (updated):
    - `id`: integer (auto-increment primary key)
    - `name`: string (required)
    - `level`: string (required)
    - `teacher_id`: integer (foreign key referencing the `Teacher` entity)

- **Teacher** (existing entity)
  - Attributes:
    - `id`: integer (auto-increment primary key)
    - `name`: string (required)
    - `email`: string (required, must be unique)

- **Student** (existing entity)
  - Attributes:
    - `id`: integer (auto-increment primary key)
    - Other attributes as defined previously (not detailed in this feature)

## Assumptions
- Users assigning teachers to courses are familiar with the required data format.
- The application environment supports the necessary database management systems (like SQLite) as defined previously.
- Existing records for students, courses, and teachers will not be impacted by the introduction of the relationship between courses and teachers.

## Out of Scope
- Advanced features such as unassigning teachers from courses or querying courses by teacher will not be included in this version.
- User interface components related to these functionalities are not covered; only the backend API is within scope.
- Bulk assignments of teachers to multiple courses or handling complex scenarios involving multiple teachers per course will be excluded from this initial version.