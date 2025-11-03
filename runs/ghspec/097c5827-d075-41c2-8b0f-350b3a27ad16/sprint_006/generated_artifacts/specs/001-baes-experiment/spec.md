# Feature: Add Teacher Relationship to Course Entity

---

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing `Course` and `Teacher` entities in the educational system. This relationship will allow each `Course` to be associated with a `Teacher`, facilitating improved course management and enhancing the educational experience by enabling better visibility of teaching staff associated with each course. This will streamline administrative processes and provide students with clear information about their instructors.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**:
   - **Scenario**: An admin assigns an existing teacher to a course.
   - **Expected Result**: The application successfully links the teacher to the course, and the course details reflect the updated teacher information.

2. **Retrieving Course Details with Teacher Information**:
   - **Scenario**: A user requests details of a specific course, including the assigned teacher.
   - **Expected Result**: The application returns the course details along with the teacher's name and email if the teacher is associated with the course.

3. **Handling Unassigned Course**:
   - **Scenario**: A user requests details for a course that does not have a teacher assigned.
   - **Expected Result**: The application still returns the course details but indicates that no teacher is assigned.

4. **Error on Assigning Non-existent Teacher**:
   - **Scenario**: An admin attempts to assign a non-existent teacher to a course.
   - **Expected Result**: The application returns an error message indicating that the teacher does not exist.

## Functional Requirements
1. **Assign Teacher to Course Endpoint**:
   - HTTP method: PATCH
   - Endpoint: `/courses/{courseId}/assign-teacher`
   - Request body:
     - `teacherId`: integer (required)
   - Response:
     - On success (HTTP 200):
       - JSON object confirming the teacher has been assigned.
     - On failure (HTTP 400):
       - JSON object with error message if the teacher does not exist or course ID is invalid.

2. **Retrieve Course Details with Teacher**:
   - HTTP method: GET
   - Endpoint: `/courses/{courseId}`
   - Response:
     - On success (HTTP 200):
       - JSON object containing:
         - `courseId`: integer
         - `courseName`: string
         - `level`: string
         - `teacher`: 
           - `id`: integer
           - `name`: string
           - `email`: string
     - On failure (HTTP 404):
       - JSON object with error message if the course does not exist.

3. **Database Migration**:
   - Update the `Course` entity schema to include a foreign key relationship to the `Teacher` entity.
   - Ensure that the migration process preserves existing data in the `Student`, `Course`, and `Teacher` entities.

## Success Criteria
1. At least 90% of API requests for assigning a teacher to a course are successful and return the expected response.
2. The application must handle cases where teachers are not assigned, returning relevant course details while notifying users of missing teacher information.
3. Error handling must be in place to manage attempts to link a course with a non-existent teacher, providing informative error messages.

## Key Entities
1. **Course**:
   - `id`: integer (auto-generated primary key)
   - `name`: string (required)
   - `level`: string (required)
   - `teacherId`: integer (foreign key referencing `Teacher` entity, can be null if no teacher is assigned)

2. **Teacher**:
   - `id`: integer (auto-generated primary key)
   - `name`: string (required)
   - `email`: string (required, must be in a valid format)

3. **Existing Entities**:
   - **Student**:
     - `id`: integer (auto-generated primary key)
     - `name`: string (required)

## Assumptions
1. Admin users have the necessary permissions to assign teachers to courses.
2. Course and Teacher IDs provided during API requests are valid and correspond to existing records in the database.
3. The changes to the database schema will be backward compatible, ensuring existing data integrity and functionality.

## Out of Scope
1. Frontend updates for displaying teacher assignments associated with courses.
2. Any additional functionality such as managing multiple teachers for a single course at this stage.
3. Comprehensive user authentication and authorization adjustments for teacher-course management beyond basic assignment.

Instructions for Incremental Development:
1. The new feature should EXTEND the existing system.
2. Use the SAME tech stack as previous sprints (consistency is critical).
3. Reference existing entities/models without recreating them.
4. Document changes needed in existing code (additions/modifications, NOT replacements) to accommodate this new relationship.