# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` and `Teacher` entities within the existing educational management system. By introducing this relationship, each course will be able to have one assigned teacher, which enhances the tracking and administration of course instruction. This feature aims to provide better organization of courses within the system and allow for a clearer association between teachers and the courses they oversee.

## User Scenarios & Testing
1. **Assign Teacher to Course**:
   - As an administrator, I want to assign a teacher to a specific course, so that I can ensure courses are linked to the appropriate educator.
   - Test: Validate that when an administrator assigns a valid teacher to a course, the relationship is created successfully.

2. **View Course with Teacher Information**:
   - As a student, I want to view course details, including the assigned teacher’s name, so that I can identify my educators.
   - Test: Validate that when retrieving course details, the response includes the assigned teacher’s name.

3. **Validation of Teacher Assignment**:
   - As an administrator, I want to receive an error message if I attempt to assign a non-existent teacher to a course.
   - Test: Validate that the application returns an appropriate error message when attempting to link to an invalid teacher ID.

## Functional Requirements
1. The application must allow an administrator to assign a teacher to a course:
   - **Endpoint**: `/courses/{courseId}/assign-teacher` (POST)
   - **Request Body**:
     ```json
     {
         "teacherId": "<integer>"
     }
     ```
   - **Response**:
     - Status code 200 (OK) confirming the teacher has been successfully assigned to the course.

2. The application must provide an updated API endpoint to retrieve details of a course including the assigned teacher:
   - **Endpoint**: `/courses/{courseId}` (GET)
   - **Response**:
     - Status code 200 (OK) with a JSON object containing course details, including the `teacher` object with its `name`.

3. The application must validate input data when assigning a teacher:
   - If the `teacherId` does not correspond to an existing teacher, the application must return a status code 404 (Not Found) with an appropriate error message.

4. The SQLite database schema must be updated to include a foreign key relationship in the `courses` table that references the `teachers` table:
   - **Table Name**: `courses`
   - **Updated Fields**:
     - `teacher_id`: Integer (Foreign Key referencing `teachers.id`, nullable)

5. A database migration must be created to include the `teacher_id` column in the `courses` table while preserving existing data for `Students`, `Courses`, and `Teachers`.

## Success Criteria
1. Users can successfully assign a teacher to a course by submitting a valid request, receiving a 200 status code with confirmation.
2. Users can retrieve course details which include valid JSON data with course information and the assigned teacher.
3. Input validation for teacher assignment works effectively, returning a 404 status code when attempting to assign a non-existent teacher ID, along with a clear error message.
4. The application initializes successfully with an updated database schema, and existing data for `Students`, `Courses`, and `Teachers` remains intact.

## Key Entities
- **Course**:
  - Attributes:
    - `id`: Integer (Primary Key, Auto-increment)
    - `name`: String (required)
    - `teacher_id`: Integer (nullable, Foreign Key referencing `teachers.id`)

- **Teacher**:
  - Attributes:
    - `id`: Integer (Primary Key, Auto-increment)
    - `name`: String (required)
    - `email`: String (required, unique)

## Assumptions
- The web application continues to operate in an environment utilizing SQLite for data persistence.
- The existing relationship and foreign key constraints in the application are properly configured to maintain referential integrity.
- Administrators have the necessary permissions to assign teachers to courses.

## Out of Scope
- UI changes necessary for administrators to manage assignments of teachers to courses—this is focused on backend functionality only.
- Functionality for handling multiple teachers per course or bulk assignments is not included in this feature.
- Notifications or alerts related to assignment status or changes to course-teacher associations are not addressed in this iteration.