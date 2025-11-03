# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the **Course** entity and the newly introduced **Teacher** entity. By enabling courses to be associated with teachers, this feature enhances the overall organization and management of courses within the Student Management Web Application. This relationship will allow for improved tracking of course assignments, administrative oversight, and facilitate better communication regarding course-related matters. The goal is to streamline the process of associating educators with their respective courses, thereby enhancing the usability and functionality of the application.

## User Scenarios & Testing
1. **Scenario 1: Associate a Teacher with a Course**
   - A user submits a request to associate an existing **Course** with a **Teacher**.
   - **Test Case:** Verify that the course is successfully updated with the teacher's details and a success response is returned.

2. **Scenario 2: Associate a Course with a Non-Existent Teacher**
   - A user attempts to associate a course with a teacher ID that does not exist.
   - **Test Case:** Ensure the API returns an appropriate error message indicating that the teacher cannot be found.

3. **Scenario 3: Verify Course to Teacher Association**
   - A user fetches the details of a course to confirm it correctly reflects its associated teacher(s).
   - **Test Case:** Validate that the course details include the correct teacher information.

4. **Scenario 4: Database Migration Verification**
   - Verify that the migration to include the teacher relationship in the Course entity does not affect existing data for Students and Courses.
   - **Test Case:** Confirm that the existing Student and Course data remains intact after the database schema update.

## Functional Requirements
1. **Associate Teacher with Course**
   - Endpoint: `POST /courses/{courseId}/assignTeacher`
   - Request Body: Contains `teacherId` (integer, required).
   - Response: Returns the updated Course object in JSON format, confirming the association with the teacher.

2. **Schema Update**
   - Update the existing database schema for the **Course** entity to include a new foreign key field:
     - `teacher_id`: Integer (nullable, referencing the Teacher entity).
   - Conduct a database migration that preserves all existing data for Students, Courses, and Teachers while adding the relationship to the schema.

## Success Criteria
1. The API returns valid JSON responses upon successful association of a teacher to a course, including confirmation of the course's updated attributes.
2. It is verified that the `teacher_id` field in the Course entity is correctly linked to the Teacher entity after the migration.
3. All operations related to associating courses and teachers work correctly without errors.
4. Validation rules ensure proper handling of non-existent teacher associations, providing appropriate error messages.

## Key Entities
- **Course**
  - Existing attributes remain unchanged, with the addition of:
    - `teacher_id`: Integer (nullable, references Teacher).
  
- **Teacher**
  - Existing attributes remain unchanged.

- **Student**
  - Existing attributes remain unchanged.

## Assumptions
- Users will have knowledge of HTTP operations and JSON data format.
- The teacher association for courses is expected to handle cases where a course may not need to have a teacher (hence the nullable foreign key).
- The existing database migration procedures are properly established, ensuring that all previous data is maintained.
- The environment will continue to support the same version of libraries and frameworks as in previous sprints.

## Out of Scope
- User interface changes required for displaying or managing teacher assignments for courses.
- Advanced features such as automatically assigning teachers based on subject expertise or statistics.
- Modifications to existing Student or Teacher entities’ attributes beyond the integration of the teacher relationship with courses.
- Any changes to the existing system that do not directly relate to the association of Teachers with Courses.

--- 

### Instructions for Incremental Development
1. This new feature must EXTEND the current system, specifically by introducing the relationship between Course and Teacher without replacing existing functionalities.
2. The SAME tech stack and database practices should be adhered to as established in previous sprints for consistency.
3. Reference existing entities/models while integrating the new relationship functionality without redefining them.
4. Clearly specify how the new Course-Teacher relationship will integrate with current functionalities, particularly around data integrity and administrative capabilities.
5. Document necessary changes to existing code to include the new relationship without altering the established structure and functions of other entities.