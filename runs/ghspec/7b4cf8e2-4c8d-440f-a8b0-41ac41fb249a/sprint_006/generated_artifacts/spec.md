# Feature: Add Teacher Relationship to Course Entity

---

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity within the student management application. This relationship allows each course to be associated with a specific teacher, enabling better management of course assignments and facilitating a clearer understanding of teaching responsibilities. By implementing this feature, the system will provide enhanced functionality for academic data management, contributing to an inclusive educational experience for students and faculty alike.

## User Scenarios & Testing
1. **Assign Teacher to Course**: A user assigns a teacher to a specific course through the course management interface.
   - Test case: Validate that the selected teacher is successfully linked to the specified course.

2. **View Course Details with Teacher**: A user requests to view information about a specific course, including the assigned teacher.
   - Test case: Confirm that the course details displayed include the name of the assigned teacher, if any.

3. **Unassign Teacher from Course**: A user removes a teacher from a course.
   - Test case: Ensure that upon removal, the course no longer displays the previously assigned teacher.

4. **List All Courses with Teachers**: A user requests a list of all courses along with their respective assigned teachers.
   - Test case: Verify that the list accurately reflects each course and its associated teacher.

## Functional Requirements
1. **Course Entity Update**:
   - Add a relationship field in the Course entity allowing for a reference to the Teacher entity.
   - Each course should have an optional `teacher_id` attribute linking it to the corresponding Teacher entity.

2. **Database Schema**:
   - Update the existing Course table to include a new column:
     - `teacher_id` (integer, optional, foreign key referencing the Teacher table)
   - Ensure the migration script allows for the safe alteration of the Course table while preserving current Course and Teacher entries.

3. **API Endpoints**:
   - **PUT /courses/{course_id}/assign-teacher/{teacher_id}**: Assign a teacher to a specific course.
   - **DELETE /courses/{course_id}/unassign-teacher**: Remove the teacher assignment from a course.
   - **GET /courses/{course_id}**: Retrieve the details of a specific course, including the assigned teacher.
   - **GET /courses**: Retrieve a list of all courses, along with their assigned teachers.

4. **Response Format**:
   - All API responses must maintain a consistent JSON format that includes confirmation messages for assignments and removals, as well as detailed information for course retrievals.

## Success Criteria
- Successfully assigning and unassigning teachers to/from courses without any errors.
- Confirm that the API accurately returns course details that reflect any assigned teachers.
- The migration successfully updates the Course table to accommodate the new relationship while preserving existing data.
- Ensure all API responses remain consistent and structured in JSON format.

## Key Entities
- **Course**:
  - ID (integer, auto-generated, primary key)
  - Name (string, required)
  - Level (string, required)
  - `teacher_id` (integer, optional, foreign key)

- **Teacher**:
  - ID (integer, auto-generated, primary key)
  - Name (string, required)
  - Email (string, required, unique)

- **Student**:
  - ID (integer, auto-generated)
  - Other fields as previously defined

## Assumptions
- The application will ensure that the `teacher_id` properly references the Teacher table’s ID, maintaining referential integrity.
- Users have necessary permissions to assign and unassign teachers to/from courses.
- The system will enforce the relationships and accurately manage records without loss of existing data.

## Out of Scope
- Enhancements to user interface elements for course and teacher management.
- Creation of automated notifications or alerts related to teacher assignments.
- Modifications to course grading or performance metrics linked to teachers.

This feature builds upon the previous sprint's creation of the Teacher entity, extending the capabilities of the Course entity by establishing a relationship that enhances academic data management and fosters a comprehensive educational environment. 

Previous Sprint Tech Stack:
No tech stack defined in previous plan

Previous Entities/Models:
- **Teacher**:
  - ID (integer, auto-generated, primary key)
  - Name (string, required)
  - Email (string, required, unique)

- **Student**:
  - ID (integer, auto-generated)
  - Other fields as previously defined

- **Course**:
  - ID (integer, auto-generated)
  - Name (string, required)
  - Level (string, required)

Instructions for Incremental Development:
1. The new feature should EXTEND the existing system
2. Use the SAME tech stack as previous sprint (consistency is critical)
3. Reference existing entities/models - don't recreate them
4. Specify how new components integrate with existing ones
5. Document what changes are needed to existing code (additions/modifications, NOT replacements)