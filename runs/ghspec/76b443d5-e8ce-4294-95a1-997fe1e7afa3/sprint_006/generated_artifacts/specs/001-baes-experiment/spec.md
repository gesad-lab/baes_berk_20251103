# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` entity and the newly created `Teacher` entity. This relationship will allow each course to be associated with a specific teacher, enhancing the educational management system's capability to track which teacher is responsible for which course. By implementing this feature, users will be able to better manage course assignments, link teacher information with courses, and ultimately improve the effectiveness of course delivery and administration.

## User Scenarios & Testing
1. **Scenario 1: Assign a Teacher to a Course**
   - **Given** a course and an existing teacher,
   - **When** an admin assigns the teacher to the course,
   - **Then** the course should successfully reflect the assigned teacher's details.

2. **Scenario 2: Retrieve Course Details with Teacher Information**
   - **Given** a course assigned to a teacher,
   - **When** a user requests the details of that course,
   - **Then** the response should include the course information along with the assigned teacher's details.

3. **Scenario 3: Assign a Teacher to Non-Existent Course**
   - **Given** a non-existing course ID,
   - **When** an admin attempts to assign a teacher to this course,
   - **Then** the response should indicate that the course does not exist.

4. **Scenario 4: Remove Teacher from Course**
   - **Given** a course with an assigned teacher,
   - **When** an admin removes the teacher from the course,
   - **Then** the course should no longer show the association with that teacher.

## Functional Requirements
1. The application must update the `Course` entity to include a relationship to the `Teacher` entity, which will allow a single teacher to be assigned to each course.
  
2. The database schema must be modified to include a new column in the `Course` table:
   - `teacher_id` (foreign key, references the `Teacher` entity).

3. The application must include an API endpoint to assign a teacher to an existing course with the following:
   - Method: PATCH
   - Endpoint: `/courses/{course_id}/assign-teacher`
   - Request Body: JSON object containing `teacher_id` (integer, required).
   - Response: JSON object confirming the assignment of the teacher to the course.

4. The application must include a mechanism to retrieve a course's details, now including teacher information, with the following:
   - Method: GET
   - Endpoint: `/courses/{course_id}`
   - Response: JSON object containing course details including the associated teacher's information.

5. The application must include an API endpoint to remove a teacher from a course:
   - Method: PATCH
   - Endpoint: `/courses/{course_id}/remove-teacher`
   - Response: JSON object confirming the removal of the teacher from the course.

6. The database migration process must ensure that existing `Student`, `Course`, and `Teacher` data remains intact during schema updates.

## Success Criteria
1. The application should successfully assign a teacher to a course when a valid `teacher_id` is provided.
2. The application should return a response confirming the assignment of the teacher to the course.
3. When retrieving course details, the response must include the correct teacher's details if assigned.
4. Removing a teacher from a course must update the course successfully without losing any existing data.
5. No data loss must occur during the database migration process.

## Key Entities
- **Course**
  - Existing fields remain unchanged.
  - New field: `teacher_id` (foreign key referencing `Teacher`).

- **Teacher**
  - Existing fields remain unchanged.

- **Student**
  - Existing fields remain unchanged.

## Assumptions
1. The existing database structure can support the addition of the `teacher_id` field without significant modifications to other tables.
2. API endpoints will be tested using tools like Postman or cURL, similar to the previous sprint.
3. Input validation will be implemented to ensure the accuracy of the `teacher_id` being assigned to the course.
4. The current technology stack used in prior sprints continues to be applicable for this feature implementation.

## Out of Scope
1. User interface changes related to displaying teacher information on the course management screen.
2. Advanced functionalities, such as allowing multiple teachers per course or tracking teacher performance.
3. Analytics or reporting features based on the course-teacher relationship.
4. Deployment to production; this feature will focus on local development and testing only.