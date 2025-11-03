# Feature: Add Course Relationship to Student Entity

---

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing **Student** entity and the newly introduced **Course** entity. By implementing this relationship, we enable students to be linked with one or more courses they are enrolled in, enhancing data management and the overall functionality of the Student Management Web Application. This update is crucial in allowing educators and administrators to better track student enrollments and course participation.

## User Scenarios & Testing
1. **Scenario 1: Enroll Student in Course**
   - A user sends a request to enroll a student in a course by providing the Student ID and Course ID.
   - **Test Case:** Ensure that a valid enrollment is created and a success response is returned with the enrollment details.

2. **Scenario 2: Retrieve Enrolled Courses for a Student**
   - A user sends a request to retrieve courses in which a specific student is enrolled by providing the Student ID.
   - **Test Case:** Verify that the API correctly returns a list of course objects corresponding to that student.

3. **Scenario 3: Invalid Enrollment Attempt**
   - A user attempts to enroll a student into a course with an invalid Student ID or Course ID.
   - **Test Case:** Ensure the API returns an error indicating the Student ID or Course ID is invalid.

4. **Scenario 4: Database Migration Verification**
   - Verify that the existing Students and Courses data remains intact after the database schema is updated to include the relationship.
   - **Test Case:** Confirm the integrity of both the Student and Course data following the schema update.

## Functional Requirements
1. **Enroll Student in Course**
   - Endpoint: `POST /enrollments`
   - Request Body: Contains the `student_id` (string, required) and `course_id` (string, required).
   - Response: Returns the created enrollment object in JSON format, confirming the associations.

2. **Retrieve Enrolled Courses for Student**
   - Endpoint: `GET /students/{student_id}/courses`
   - Response: Returns a JSON array of course objects that the student is enrolled in.

3. **Schema Update**
   - Update the existing database schema to add a relationship between Students and Courses. This will require:
     - A new join table named `Enrollments` with the following fields:
       - `id`: Integer (automatically generated primary key)
       - `student_id`: Integer (foreign key referencing Student)
       - `course_id`: Integer (foreign key referencing Course)
   - Conduct a database migration that preserves existing Student and Course data while adding the new relationship.

## Success Criteria
1. The API returns valid JSON responses for all operations related to student enrollments in courses.
2. The database schema is updated successfully, and all existing Student and Course data remains intact after the migration.
3. All CRUD operations (Create, Read) for student enrollments function correctly without errors.
4. Validation rules ensure that both Student ID and Course ID are required upon enrollment, and appropriate error messages are provided for invalid inputs.

## Key Entities
- **Enrollment**
  - Attributes:
    - `id`: Integer (automatically generated primary key)
    - `student_id`: Integer (foreign key)
    - `course_id`: Integer (foreign key)
  
- **Student**
  - Existing attributes remain unchanged.

- **Course**
  - Existing attributes remain unchanged.

## Assumptions
- Users are familiar with HTTP operations and JSON format.
- All existing IDs for students and courses provided during enrollment requests are valid.
- The application will maintain consistency with the existing tech stack used in the previous sprint.
- The environment will continue to support the same version of libraries and frameworks implemented in the previous sprint.

## Out of Scope
- User interface changes to display course enrollments.
- Advanced features such as enrollment expiration or course completion tracking.
- Integration with external systems for course management or student records.
- Modifications to the Student or Course entities' existing attributes, apart from establishing relationships.

--- 

### Instructions for Incremental Development
1. This new feature should EXTEND the existing system and not replace any existing functionalities.
2. Use the SAME tech stack as defined in the previous sprint to ensure consistency in the application.
3. Reference existing entities/models, like Student and Course, for the relationship but do not redefine them.
4. Clearly specify how the new Enrollment entity integrates with existing features and models of the application, particularly how students and courses are linked.
5. Document any small changes needed to existing code to support the addition of the Enrollment entity without affecting the overall system operation.