# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` and `Teacher` entities within the existing educational management system. This relationship allows each `Course` to be associated with a specific `Teacher`, streamlining course management and enabling better tracking of who is responsible for each course. By implementing this feature, we aim to enhance the usability of the system for administrators and improve resource allocation within the educational framework.

## User Scenarios & Testing
1. **Scenario 1**: A user links a teacher to an existing course.
   - **Test**: Given an existing course ID and a teacher ID, the system should successfully establish a relationship and return a confirmation of the update.

2. **Scenario 2**: A user tries to link a course to a non-existing teacher.
   - **Test**: The system should return an error indicating that the specified teacher does not exist.

3. **Scenario 3**: A user checks the database schema to confirm the relationship between Course and Teacher without disrupting existing data.
   - **Test**: The `Course` table should be updated to include a foreign key reference to the `Teacher` table without any loss of data in existing `Student` and `Course` tables.

4. **Scenario 4**: A user retrieves all courses for a specific teacher.
   - **Test**: Given a teacher ID, the system should return all courses associated with that teacher.

## Functional Requirements
1. The `Course` entity must be updated to include a relationship to the `Teacher` entity:
   - **Field**: `teacher_id` (Integer, Optional Foreign Key referencing `Teacher.id`)

2. The system must provide an endpoint to associate a teacher with an existing course:
   - **Endpoint**: `PATCH /courses/{course_id}/assign-teacher`
   - **Request body** must include a JSON object containing `{ "teacher_id": integer }`.

3. Update the database schema to include the foreign key relationship:
   - Modify the `Courses` table to add the `teacher_id` column as a foreign key.
   - The migration process must ensure that existing data in `Student` and `Course` tables remains intact.

4. The system must allow for retrieval of all courses associated with a specific teacher:
   - **Endpoint**: `GET /teachers/{teacher_id}/courses`
   - The system should return a list of course objects associated with the specified teacher.

## Success Criteria
1. A user must be able to successfully link a teacher to a course, and the system must return a confirmation message.
2. A user must receive an error message when attempting to link a non-existing teacher to a course.
3. The database schema must include the new `teacher_id` field in the `Courses` table without any loss of data in existing tables.
4. The retrieval endpoint should return the correct list of courses for a given teacher.

## Key Entities
- **Teacher**:
  - `id` (Integer, Primary Key, Auto-increment)
  - `name` (String, Required)
  - `email` (String, Required)

- **Course** (Updated):
  - `id` (Integer, Primary Key)
  - `name` (String, Required)
  - `level` (String, Required)
  - `teacher_id` (Integer, Foreign Key to Teacher)

- **Student** (Existing):
  - `id` (Integer, Primary Key)
  - `name` (String, Required)
  - Other existing fields...

## Assumptions
- The existing database system can accommodate new foreign key relationships without negatively impacting performance or existing operations.
- Users will have access to the required permissions to update courses and link them to teachers.
- The migration process will preserve current relationships and ensure data integrity across all relevant tables.

## Out of Scope
- User interface components for assigning teachers to courses.
- Advanced functionalities, such as implementing role-based permissions for course management.
- Any features related to detailed reporting or analytics on teacher performance or course effectiveness. 

--- 

**Incremental Development Context**:
1. This feature should EXTEND the existing system.
2. Utilize the SAME tech stack as the previous sprint (consistency is critical).
3. Reference existing entities/models and avoid recreating them.
4. Specify how the new teacher relationship integrates with existing Course and Teacher components.
5. Document necessary additions or modifications to existing code, not replacements.