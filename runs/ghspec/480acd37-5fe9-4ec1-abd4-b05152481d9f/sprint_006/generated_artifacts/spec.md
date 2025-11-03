# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity, allowing each course to have an associated teacher. This enhancement serves to improve the functionality of the educational management system by enabling better tracking of course assignments and enhancing the overall organization. The addition of this relationship aligns with our goal of creating a comprehensive platform for managing educational resources, thereby benefiting administration and students alike.

## User Scenarios & Testing
1. **Assign a Teacher to a Course**: An admin user can assign a teacher to a specific course. The system should confirm the successful assignment of the teacher to that course.
   - **Test**: Ensure that after assigning a teacher to a course, the course details reflect the assigned teacher correctly.

2. **Fetch Course Details with Teacher Information**: An admin user can request the details of a course, including the assigned teacher's information. The response should include the relevant course and teacher details.
   - **Test**: Ensure that a valid request returns a JSON object containing the course and its associated teacher data.

3. **Validate Teacher Assignment to Course**: An admin user attempts to assign a teacher to a course that exceeds the system's limit (e.g., assigning a teacher already assigned to another course). The system should prevent the assignment and return appropriate error messages, if applicable.
   - **Test**: Confirm that an error is returned if attempting to assign a teacher to an incompatible course configuration.

## Functional Requirements
1. **Database Changes**:
   - Modify the existing Course table to include a new column:
     - `teacher_id`: Foreign key referencing the Teacher entity (integer, nullable), allowing a course to be linked to a teacher.

2. **API Endpoints**:
   - **PATCH /courses/{course_id}/assign-teacher**: This endpoint will allow for the assignment of a teacher to a course.
     - Request body: `{ "teacher_id": "integer" }`
     - Response: `200 OK` with a success message confirming the assignment.

   - **GET /courses/{course_id}**: This endpoint retrieves details of a specific course, including its assigned teacher.
     - Response: `200 OK` with an object containing course details, including teacher information if assigned.

3. **Field Validation**:
   - The system must validate that the `teacher_id` provided during teacher assignment exists and corresponds to a valid teacher in the database.
   - The course can optionally have no teacher assigned (i.e., the `teacher_id` can be nullable).

4. **Database Migration**:
   - The migration process must alter the existing Course table to add the `teacher_id` column without affecting existing data related to the Students or Teachers.

## Success Criteria
- The new relationship between Course and Teacher can be established and retrieved successfully using specified API endpoints.
- The system maintains strict validation, returning meaningful error messages for invalid `teacher_id` assignments.
- All API responses should provide accurate and valid JSON formatted data relevant to course and teacher details.
- The migration process results in the successful modification of the Course table while preserving the integrity of existing data.

## Key Entities
- **Course**
  - `id`: Unique identifier for the Course entity (integer).
  - `title`: The title of the course (string).
  - `teacher_id`: Foreign key referencing the Teacher entity (integer, nullable).

- **Teacher**
  - `id`: Unique identifier for the Teacher entity (integer).
  - `name`: The name of the teacher (string).
  - `email`: The email of the teacher (string).

## Assumptions
- The existing application infrastructure supports the alteration of existing tables and ensures proper migration without data loss.
- Admin users will provide valid `teacher_id` information during the course assignment process.
- The application environment has appropriate foreign key constraints to enforce referential integrity.

## Out of Scope
- The scope excludes changes to the user interface or experience; focus remains solely on backend functionality for managing course and teacher relationships.
- The process of unassigning a teacher from a course or any other complex logic regarding teacher-course assignments is not included.
- Features related to course evaluations, attendance tracking, or performance metrics associated with courses or teachers are not part of this feature; it specifically targets the relationship between teachers and courses.