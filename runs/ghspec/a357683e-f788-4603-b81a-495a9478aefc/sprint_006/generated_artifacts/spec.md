# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the newly created Teacher entity. By associating a teacher with specific courses, the application will enhance its ability to track teaching assignments, manage course information more effectively, and improve the overall educational experience by clearly defining the responsibilities of teachers within the system.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**
   - **Scenario**: An admin wants to assign a teacher to a specific course.
   - **Test**: Validate that the system allows the assignment of a teacher to a course and correctly updates the course record in the database.

2. **Retrieving Courses with Their Assigned Teacher**
   - **Scenario**: A user wants to view the details of a course along with its assigned teacher.
   - **Test**: Confirm that the application retrieves the course’s information, including the teacher's name, in a structured JSON format when queried.

3. **Removing a Teacher from a Course**
   - **Scenario**: An admin decides to remove a teacher's assignment from a course.
   - **Test**: Ensure that the application correctly removes the teacher from the course record while preserving other course data.

4. **Querying Courses of a Specific Teacher**
   - **Scenario**: A user wants to list all courses taught by a specific teacher.
   - **Test**: Validate that the application returns all courses associated with that teacher in an appropriate format.

## Functional Requirements
1. **Assign a Teacher to a Course**:
   - **Method**: PATCH
   - **Endpoint**: `/courses/{course_id}/assign-teacher`
   - **Request Body**:
     - `teacher_id`: integer (required, must reference an existing Teacher)
   - **Response**: 200 OK with JSON confirmation of the updated course including the assigned teacher details.

2. **Retrieve Course with Assigned Teacher**:
   - **Method**: GET
   - **Endpoint**: `/courses/{course_id}`
   - **Response**: 200 OK with JSON object that includes course data along with the assigned teacher's name.

3. **Remove Teacher from a Course**:
   - **Method**: PATCH
   - **Endpoint**: `/courses/{course_id}/remove-teacher`
   - **Response**: 200 OK with JSON confirmation of the updated course with no assigned teacher.

4. **Query Courses by Teacher**:
   - **Method**: GET
   - **Endpoint**: `/teachers/{teacher_id}/courses`
   - **Response**: 200 OK with a JSON array of courses associated with the specified teacher.

5. **Database Schema Update**:
   - Alter the existing `Course` table to include a new column:
     - `teacher_id`: integer, foreign key referencing Teacher(id), allows null values for courses that do not have a teacher assigned.
   - Ensure the database migration preserves existing data for Students, Courses, and Teachers while accurately implementing the new relationship.

## Success Criteria
- The application must allow the successful assignment and retrieval of a teacher for a course through the dedicated endpoints and confirm the actions with relevant JSON data.
- Removal of a teacher from a course must succeed without affecting other course records or teacher data.
- Querying for courses associated with a specific teacher must return accurate data including all relevant course details.
- The database schema migration must occur without data loss and maintain existing integrity across Student, Course, and Teacher tables.

## Key Entities
- **Teacher**
  - `id`: Integer (primary key)
  - `name`: String (required)
  - `email`: String (required, must be unique)
- **Course** (existing)
  - `id`: Integer (primary key)
  - `name`: String (required)
  - `teacher_id`: Integer (nullable, foreign key to Teacher.id)
- **Student** (existing)

## Assumptions
- The current data model can incorporate the new relationship without significant restructuring.
- The format and retrieval of existing data from the Course entity are well established and can smoothly integrate this new feature.
- Validation for the presence of assigned teachers will be managed by existing systems ensuring integrity during the assignment process.

## Out of Scope
- Changes to the user interface to display teacher assignments in course details.
- Updates to reporting features that analyze teacher performance relative to course assignments.
- Extended functionalities such as notifications or reminders related to course assignments or changes in teachings.