# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` and `Teacher` entities. By enabling courses to have designated teachers, the application will better manage educational roles, facilitate course management, and enhance overall functionality. This relationship is critical for future features such as course assignments and teacher assignments while ensuring that existing functionalities related to `Student` and `Course` remain intact.

## User Scenarios & Testing
1. **Assign a Teacher to a Course**: An admin user assigns a teacher to a course, which should update the course's record successfully.
2. **Assign a Teacher to a Non-Existent Course**: An attempt to assign a teacher to a course that does not exist should return an error response indicating the course is not found.
3. **Retrieve Course with Teacher Information**: When retrieving course information, the details of the assigned teacher should be included in the response.
4. **Database Migration for Teacher-Course Relationship**: On application startup, the database schema must be updated to include a foreign key relationship without affecting existing `Student`, `Course`, or `Teacher` data.

## Functional Requirements
1. **Assign a Teacher to a Course**:
   - Endpoint: `POST /courses/{course_id}/assign-teacher/{teacher_id}`
   - Response: 
     - `200 OK` with a message confirming the assignment if successful.
     - `404 Not Found` if the course does not exist.
  
2. **Retrieve Course Information**:
   - Endpoint: `GET /courses/{course_id}`
   - Response: `200 OK` with course details including `teacher` information when a valid course ID is provided.

3. **Database Migration**:
   - Update the database schema to modify the `Course` table to include a new column:
     - **teacher_id**: Reference to `Teacher` entity, nullable to accommodate existing records.
   - The migration must preserve existing data within `Student`, `Course`, and `Teacher` entities, ensuring no data loss occurs.

## Success Criteria
- The system must return a `200 OK` response when a teacher is successfully assigned to a course, along with a confirmation message.
- The system must return a `404 Not Found` error when trying to assign a teacher to a course that does not exist.
- When retrieving a course, the response must successfully include the assigned teacher's details if a teacher is assigned.
- The database schema must successfully include a foreign key reference for the `teacher_id` in the `Course` table without causing data loss.

## Key Entities
- **Course** (Modified entity)
  - **teacher_id**: Reference to `Teacher`, nullable

- **Teacher** (Existing entity)
  - **name**: String, required
  - **email**: String, required and must be unique

- **Student** (Existing entity)
  - No changes are required.

## Assumptions
- The existing database management system will support foreign key relationships.
- The data integrity across the `Course`, `Student`, and `Teacher` entities will be maintained during the migration.
- The system will handle null values for `teacher_id` for courses that do not have a teacher assigned.

## Out of Scope
- User interface changes for managing teacher assignments to courses are outside the scope of this feature.
- Advanced functionalities, such as multiple teachers per course or their credential checks, are not included.
- Backend processes for notifying teachers about their assigned courses is not part of this feature.

## Instructions for Incremental Development:
1. The new feature should EXTEND the existing system by integrating the teacher relationship into the `Course` entity.
2. Utilize the SAME database and data management practices as in the previous sprint to ensure consistency.
3. Reference existing entities/models ensuring alignment without recreating them.
4. Clearly specify database migration protocols to include the new `teacher_id` column in the `Course` table while preserving existing data.
5. Document any necessary additions and modifications to the current codebase for integrating the `teacher_id` foreign key into the `Course` entity.