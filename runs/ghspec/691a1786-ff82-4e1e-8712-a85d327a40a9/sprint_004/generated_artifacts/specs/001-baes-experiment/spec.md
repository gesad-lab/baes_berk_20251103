# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities within the existing student management application. This relationship will enable each Student to be associated with one or more Courses, fulfilling the business need to track student enrollments and academic pathways effectively. By incorporating this capability, the application can provide enhanced support for functionalities such as course registrations and student progress monitoring.

## User Scenarios & Testing
1. **Associating a Student with a Course**:
   - User submits a request to enroll a student in a specified course by providing the student ID and course ID.
   - Successful enrollment returns the updated student details, including the list of associated courses.

2. **Retrieving Student Courses**:
   - User requests to view all courses associated with a particular student by providing the student ID.
   - System returns a list of courses that the student is enrolled in, confirming the relationship.

3. **Removing a Course from a Student**:
   - User submits a request to remove a specific course from a student's list of courses by providing student ID and course ID.
   - Successful removal returns the updated student details confirming the course has been removed.

## Functional Requirements
1. **Enroll Student in Course**:
   - An endpoint must be provided to enroll a student in a course that accepts a JSON payload containing the student ID and course ID.
   - Must return the updated student details in JSON format after successful enrollment.

2. **Retrieve Student's Courses**:
   - An endpoint must be available to retrieve all courses associated with a given student by student ID.
   - Must return HTTP 200 with the list of courses if the student exists or HTTP 404 if the student does not exist.

3. **Remove Course from Student**:
   - An endpoint must be created to disassociate a course from a student.
   - Requires student ID and course ID in the request body.
   - Must return the updated student details in JSON format upon successful removal.
   - Should return HTTP 404 if the student or course does not exist.

4. **Database Schema Update**:
   - The database must be updated to include a many-to-many relationship between Students and Courses.
   - A join table named `StudentCourse` will be introduced with the following fields:
     - `student_id`: Integer, Foreign key referencing Student.
     - `course_id`: Integer, Foreign key referencing Course.

5. **Database Migration**:
   - The migration process must create the new `StudentCourse` table while preserving existing data in both the Student and Course tables. 

## Success Criteria
- The application can enroll a student in a course and return the updated student details in under 2 seconds.
- The application retrieves a list of courses for a student successfully, returning accurate information, or a 404 error if the student does not exist.
- The application removes a course from a student and returns the updated student details in under 2 seconds.
- Database migration successfully creates the `StudentCourse` join table without losing or corrupting existing Student or Course data.

## Key Entities
- **StudentCourse**:
  - `student_id`: Integer, Foreign key referencing Student.
  - `course_id`: Integer, Foreign key referencing Course.

## Assumptions
- Users have internet access to make API requests to the web application.
- Student and Course IDs provided in requests are valid and match existing entries in their respective tables.
- The application will be hosted on a server capable of running the same technology stack as the previous sprint.

## Out of Scope
- User authentication and authorization processes related to enrolling in courses are outside the scope of this feature.
- Validation of unique student enrollment per course will not be included in this implementation.
- Management of course capacity or restrictions on the number of courses will not be addressed in this feature.
- Advanced error handling or notifications for enrollment limits will not be part of this scope.