# Feature: Add Teacher Relationship to Course Entity

---
IMPORTANT: INCREMENTAL DEVELOPMENT CONTEXT

This is sprint 6 of an incremental development process. You must build UPON the existing system, not replace it.

Previous Sprint Specification:
# Feature: Create Teacher Entity

---

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing Course entity and the newly created Teacher entity. This will enable each course to be assigned to a specific teacher, enhancing the system's ability to manage educational resources effectively. By embedding this relationship, the application will provide better organization of course information and facilitate teacher-student communication.

## User Scenarios & Testing
1. **Assign Teacher to Course**
   - As an admin, I want to assign a teacher to a course so that the course can be directly linked to the responsible educator.
   - **Testing**: Validate that the system allows assignment of a teacher to a course and returns the updated course object.

2. **Retrieve Course Information**
   - As a user, I want to see the details of a course, including the assigned teacher’s information, to understand who is teaching the course.
   - **Testing**: Ensure that the course details returned include both the course information and the corresponding teacher’s name and email.

3. **Error Handling for Assignment**
   - As a user, I want to receive appropriate error messages if I attempt to assign a teacher that does not exist or if there is an issue with the assignment operation.
   - **Testing**: Verify that clear, actionable error messages are returned when invalid teacher IDs are provided during the assignment.

## Functional Requirements
1. **Course-Teacher Relationship**
   - Modify the existing Course entity to include a new field:
     - `teacher_id`: Integer (foreign key referencing the Teacher entity).

2. **Database Schema Update**
   - Update the database schema to support the relationship between Course and Teacher. This involves:
     - Creating a foreign key constraint on the `teacher_id` field in the Course table that references the `id` field in the Teacher table.

3. **Database Migration**
   - Execute a database migration that alters the existing Course table to add the `teacher_id` column while preserving all existing data in the Student, Course, and Teacher tables.

4. **API Endpoints**
   - **PATCH /courses/{courseId}**
     - The endpoint must accept a JSON body containing the `teacher_id` to assign a teacher to a course.
     - Upon successful assignment, return the updated course object, including the teacher’s details.

   - **GET /courses/{courseId}**
     - Update the response to also return the assigned teacher's details (name and email) alongside existing course information.

5. **JSON Responses**
   - Maintain JSON format for API responses, confirming successful teacher assignment and accurate retrieval of course details, including teacher information.

## Success Criteria
- The system must successfully allow teachers to be assigned to courses and reflect this in course data.
- Course details retrieved must accurately include information about the assigned teacher.
- The database migration must complete without losing or altering existing Student or Teacher data.

## Key Entities
- Updated **Course**
  - `id`: Integer (Automatically generated, primary key)
  - `teacher_id`: Integer (foreign key referencing Teacher)
  - Other existing fields...

- **Teacher** (no changes needed for existing fields)
  - `id`: Integer (Automatically generated, primary key)
  - `name`: String (required)
  - `email`: String (required)

## Assumptions
- Admin users will understand the implications of assigning a teacher to a course and will provide valid teacher IDs.
- The new relationship will not conflict with existing course functionalities and can be integrated smoothly.
- Proper foreign key constraints will be enforced to maintain referential integrity.

## Out of Scope
- Detailed functionalities related to teacher roles, responsibilities, or performance tracking within the course context will not be covered in this scope.
- User interface changes to display the teacher course assignments will be addressed in future iterations after the relationship is established.
- Comprehensive validation rules beyond the primary teacher assignment functionality are deferred for future consideration.

Previous Sprint Tech Stack:
No tech stack defined in previous plan

Previous Entities/Models:
- **Teacher**
  - `id`: Integer (Automatically generated, primary key)
  - `name`: String (required)
  - `email`: String (required)

- Updated **Course**
  - `id`: Integer (Automatically generated, primary key)
  - `teacher_id`: Integer (foreign key referencing Teacher)
  - Other existing fields...

Instructions for Incremental Development:
1. The new feature should EXTEND the existing system.
2. Use the SAME tech stack as previous sprint (consistency is critical).
3. Reference existing entities/models - don't recreate them.
4. Specify how new components integrate with existing ones.
5. Document what changes are needed to existing code (additions/modifications, NOT replacements).