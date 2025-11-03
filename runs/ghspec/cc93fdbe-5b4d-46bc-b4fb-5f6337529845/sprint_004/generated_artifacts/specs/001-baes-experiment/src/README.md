# README.md

# Project Title

## Introduction

This README provides an overview of the functionality and setup of the project, along with migration details and recent changes to the database schema.

## Migration and Model Changes

### New Relationship Between Students and Courses

To support the assignment of courses to students, a many-to-many relationship has been established between the `Student` and `Course` entities via a new table named `student_courses`.

#### Database Schema Changes

- **New Table**: `student_courses`
  - **Attributes**:
    - `student_id`: integer (references `Student.id`)
    - `course_id`: integer (references `Course.id`)
  
This change allows for the capability of associating multiple courses with a student and vice versa. The migration has been implemented to ensure that existing data within the `Student` and `Course` tables remains unchanged while a new relationship table has been created without data loss.

#### Migration Process

1. **Create Migration Script**: A database migration script has been created to update the database schema.
2. **Verify Data Integrity**: It is confirmed that the existing `Student` and `Course` data remains intact after migration.
3. **Run Migration**: The migration can be executed using [Your Migration Tool] to establish the new relationships.

### API Endpoints

The following API endpoints support the new functionality related to student-course relationships:

1. **Assign Courses to a Student**
   - **Endpoint**: `POST /students/{student_id}/courses`
   - **Request Body**: A JSON object containing `course_id` (integer, required).
   - **Response**: A JSON object confirming the assignment of the course to the student.

2. **Retrieve Student Courses**
   - **Endpoint**: `GET /students/{student_id}/courses`
   - **Response**: A JSON array containing details of courses the student is enrolled in (ID, name, level).

### Error Handling

- **Invalid Course Assignment**: If a user attempts to assign a course that does not exist, the application will respond with an appropriate error message indicating that the provided course ID is invalid.

### User Scenarios & Testing

1. **Assign Courses to a Student**:
   - Scenario: A user wants to add courses to a student's profile.
   - Test: Verify that the application accepts valid course IDs to associate with a student and confirms the changes in the student record.

2. **Retrieve Student Courses**:
   - Scenario: A user wants to view a list of courses assigned to a specific student.
   - Test: Verify that the application returns the correct course details for a student when requested.

3. **Error Handling for Invalid Course IDs**:
   - Scenario: A user attempts to assign a course that does not exist to a student.
   - Test: Verify that the application responds with an appropriate error message indicating that the course ID is invalid.

## Conclusion

This update includes important functionality related to the management of student-course relationships, which enhances the usability of the project. Please refer to the other sections of this README for more details on setup and usage.