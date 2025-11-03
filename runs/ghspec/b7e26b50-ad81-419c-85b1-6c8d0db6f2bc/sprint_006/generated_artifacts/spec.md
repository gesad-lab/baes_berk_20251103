# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the Teacher entity within the application. This enhancement will enable each Course to be associated with a single Teacher, thereby streamlining the process of course management and facilitating better tracking of course assignments. By implementing this relationship, we will meet the users' needs for improved organization and accessibility of course and teacher data.

## User Scenarios & Testing
1. **User Scenario: Assign a Teacher to a Course**
   - As an administrator, I want to associate a teacher with a specific course to ensure that every course has a designated educator.
   - **Test**: Verify that a PATCH request to the `/courses/{id}` endpoint with a `teacher_id` correctly updates the course and establishes the relationship.

2. **User Scenario: Course without a Teacher**
   - As a user, I want to view courses that currently do not have any assigned teachers, so that I can easily identify which courses need assignments.
   - **Test**: Ensure a GET request to the `/courses` endpoint returns courses without a `teacher_id` as part of the response.

3. **User Scenario: Invalid Teacher Assignment**
   - If I attempt to assign a non-existent teacher to a course, I want to receive an error message indicating that the teacher does not exist.
   - **Test**: Validate that a PATCH request with a non-existing `teacher_id` returns a 404 error with an appropriate message.

## Functional Requirements
1. **Assign Teacher to Course Endpoint**
   - Endpoint: `PATCH /courses/{id}`
   - Request Body:
     - `teacher_id`: integer (required, references the Teacher entity)
   - Response:
     - 200 OK with a JSON object confirming that the teacher has been successfully assigned to the course, including the updated `teacher_id`.

2. **Error Handling for Course Teacher Assignment**
   - If the specified `teacher_id` does not exist:
     - 404 Not Found with a JSON error message stating that the teacher does not exist.
   - If the course ID does not exist:
     - 404 Not Found with a JSON error message stating that the course does not exist.

3. **Database Schema Update**
   - Update the existing `Course` table by adding a new column:
     - `teacher_id`: integer, foreign key referencing the `Teacher` table.
   - Create a database migration that adds the `teacher_id` field to the `Course` table while preserving all existing data related to the `Student`, `Course`, and `Teacher` tables.

## Success Criteria
- The application allows successful assignment of a teacher to a course through the specified endpoint and returns appropriate success messages in JSON format.
- The application correctly handles error cases for invalid course or teacher IDs, providing clear messages for each scenario.
- Cover at least 70% of business logic with automated tests for the course teacher assignment functionality.
- Ensure that the database migration does not result in any data loss, preserving existing records in the `Student`, `Course`, and `Teacher` tables.

## Key Entities
- **Course**
  - Attributes (updated):
    - `id` (integer, primary key, auto-increment)
    - `name` (string, required)
    - `teacher_id` (integer, optional, references Teacher)

- **Teacher**
  - Attributes:
    - `id` (integer, primary key, auto-increment)
    - `name` (string, required)
    - `email` (string, required, unique)

- Existing Entities:
  - **Student**
    - Attributes remain unchanged.

## Assumptions
- It is assumed that the `teacher_id` provided during assignment is valid and corresponds to an existing Teacher record.
- The course ID specified in the request matches an existing Course record in the database.
- Users assigning teachers to courses have the necessary permissions to make changes in the application.

## Out of Scope
- Any functionality related to editing or deleting teacher assignments from a course is outside the scope of this feature.
- Features concerning viewing detailed course-teacher associations or courses with no teachers are not included in this specification.

This feature builds upon the existing system by extending the Course entity to introduce a new relationship with the Teacher entity, thereby enhancing the course management functionalities established in previous sprints.