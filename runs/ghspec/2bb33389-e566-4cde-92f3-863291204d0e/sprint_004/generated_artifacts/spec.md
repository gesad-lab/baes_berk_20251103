# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities. This relationship will allow a student to be enrolled in multiple courses, facilitating better management of their academic progression. By implementing this feature, the system will enhance the educational experience by bridging students with the courses they've enrolled in, enabling more comprehensive tracking and reporting of student performance.

## User Scenarios & Testing
1. **Scenario 1: Enroll Student in a Course**
   - User sends a request to enroll a student in a specific course by providing the student ID and course ID.
   - Expected Outcome: The system should successfully link the student to the course and return a confirmation response.

2. **Scenario 2: Enroll Student with Invalid Student ID**
   - User attempts to enroll a student using an invalid student ID that does not exist in the database.
   - Expected Outcome: The system should return a JSON error response indicating that the student ID is not valid.

3. **Scenario 3: Enroll Student with Invalid Course ID**
   - User attempts to enroll a student using an invalid course ID that does not exist in the database.
   - Expected Outcome: The system should return a JSON error response indicating that the course ID is not valid.

4. **Scenario 4: Retrieve Enrolled Courses for a Student**
   - User sends a request to retrieve a list of all courses the student is enrolled in.
   - Expected Outcome: The system should return a JSON response containing the list of courses for the given student.

5. **Scenario 5: Database Migration Verification**
   - On application startup or during migration, the database schema should be updated to establish the relationship between Student and Course entities.
   - Expected Outcome: The system should successfully apply the migration while preserving existing Student and Course data.

## Functional Requirements
1. **API Endpoints**:
   - **POST /students/{studentId}/courses**: Enroll a student in a course by sending a JSON body containing the course ID.
   - **GET /students/{studentId}/courses**: Retrieve a list of courses a student is enrolled in.

2. **Database Schema Changes**:
   - The existing Student table should be updated to include a many-to-many relationship with the Course table through a new join table named `StudentCourses`, which may have the following attributes:
     - student_id: integer (foreign key referencing Student)
     - course_id: integer (foreign key referencing Course)

3. **Responses**:
   - All API responses must return in JSON format.
   - Enrolling a student should return status code `201 Created` if successful.
   - Retrieval of enrolled courses should return status code `200 OK` with the courses' data.
   - Validation errors related to invalid IDs should return status code `400 Bad Request`.

## Success Criteria
- The application must allow for the enrollment of a student in a course.
- The application must successfully retrieve and list all courses a student is enrolled in.
- The database schema must include the new `StudentCourses` table while preserving all existing Student and Course data.
- All API responses must be in a valid JSON format.

## Key Entities
- **StudentCourses** (join table):
  - Attributes:
    - student_id: integer (foreign key referencing Student)
    - course_id: integer (foreign key referencing Course)

## Assumptions
- The existing database supports schema modifications such that data integrity will be maintained during migration.
- The user has access to the same environment and tech stack used in the previous sprints.
- Users interacting with the updated RESTful API understand how to process JSON data formats.

## Out of Scope
- Any updates to the authentication or authorization mechanisms related to student enrollment.
- Functions related to removing students from courses or modifying enrollment status.
- Additional features for course content management or student grading.
- User interface changes in frontend applications, if applicable.
- Any logic related to monitoring student progress within courses will not be covered in this feature.

---

This feature builds upon the previously established Course entity and introduces a clear relationship between Students and Courses while maintaining existing data and ensuring the integrity of the system.