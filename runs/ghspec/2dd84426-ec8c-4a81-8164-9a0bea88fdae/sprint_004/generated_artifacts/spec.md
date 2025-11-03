# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Student` and `Course` entities within the existing system. This relationship will allow students to be associated with one or more courses, thereby enhancing the educational functionality of the application. The integration of this relationship not only improves the ability to manage student enrollments but also ensures that future course-related features can be seamlessly developed. The existing functionalities of the `Student` and `Course` entities must remain intact.

## User Scenarios & Testing
1. **Associating a Student with a Course**: A user sends a request to associate a student with a specific course. The system should return a success response confirming the association.
2. **Failing to Associate a Student with Invalid Course ID**: A user attempts to associate a student with a course using an invalid course ID. The application should return an error response indicating that the course does not exist.
3. **Retrieving a Student's Courses**: A user requests to retrieve all courses associated with a specific student. The system should return a JSON array of all course objects linked to that student.
4. **Database Migration**: Upon starting the application, the database schema must be updated to reflect the new relationship between `Student` and `Course` without impacting existing data.

## Functional Requirements
1. **Associate a Student with a Course**:
   - Endpoint: `POST /students/:student_id/courses`
   - Request Body: `{ "course_id": "string" }` (required)
   - Response: `200 OK` with a message confirming the association.

2. **Retrieve All Courses for a Student**:
   - Endpoint: `GET /students/:student_id/courses`
   - Response: `200 OK` with a JSON array of course objects associated with the specified student.

3. **Database Migration**:
   - Update the database schema to include a new many-to-many relationship table between `Student` and `Course`, which may be called `StudentCourses`, with fields `student_id` and `course_id`.
   - The migration must preserve existing data within both `Student` and `Course` entities.

## Success Criteria
- The system must return a `200 OK` response when a student is successfully associated with a course, along with a confirmation message.
- The system must return a `404 Not Found` error when attempting to associate a student with a non-existent course ID.
- The system must return a `200 OK` response with an array of course data when retrieving all courses linked to a specific student.
- The database schema must include the new relationship table without causing data loss to existing `Student` and `Course` data.

## Key Entities
- **Student**
  - Existing entity, no changes are required.

- **Course**
  - Existing entity, no changes are required.

- **StudentCourses** (New relationship table)
  - **student_id**: Identifier of the student
  - **course_id**: Identifier of the course

## Assumptions
- The course IDs provided will always correspond to existing courses created in the previous sprint.
- The application will continue using the same database management system as the previous sprint, allowing new relationships to be added without data loss.
- Existing student and course data will not be modified during this process.

## Out of Scope
- User interface changes to display student-course associations are outside the scope of this feature.
- Advanced functionalities such as managing course completions, grading, or prerequisites are not included.
- Bulk operations to associate or dissociate multiple courses with students are not part of this feature.