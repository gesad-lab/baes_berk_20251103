# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the newly created Teacher entity. By adding this relationship, each course can have a designated teacher who is responsible for it. This enhancement will facilitate better organization of courses and improve educational management capabilities within the system.

## User Scenarios & Testing

### User Scenarios
1. **Assign a Teacher to a Course**:
   - As an admin, I want to assign a teacher to a specific course to ensure that the course has an instructor.

2. **View Course with Teacher Information**:
   - As a user, I want to view the details of a course, including the teacher assigned, to better understand who is instructing the course.

3. **Remove Teacher from a Course**:
   - As an admin, I want to remove a teacher from a course when necessary to reflect changes in course assignments.

### Testing Scenarios
1. Test that a teacher can be successfully assigned to a course, with the course metadata indicating the assigned teacher's identity.
2. Test that retrieving the details of a specific course returns the correct teacher information.
3. Test that the teacher can be removed from a course, and fetching the course details reflects that change.

## Functional Requirements
1. **Add Teacher Relationship to Course**:
   - Update the existing **Course** entity to include a relationship with the **Teacher** entity:
     - **Field**: `teacher_id` (Integer, required, Foreign Key referencing `Teacher.id`)

2. **Update the Database Schema**:
   - Modify the existing **Course** table to include a new column for the teacher reference:
     - **Column**:
       - `teacher_id`: Integer (Foreign Key, references `Teacher.id`, can be null to allow courses without assigned teachers)

3. **Database Migration Must Preserve Data**:
   - The migration process must ensure that no existing data for Courses, Students, or Teachers is affected, preserving the integrity of the current records.

4. **End Points for Managing Course-Teacher Assignment**:
   - **Assign a Teacher to a Course**:
     - **Endpoint**: `/courses/{course_id}/assign-teacher` (POST)
     - **Input**: JSON payload containing `teacher_id` (Integer, required).
     - **Output**: JSON response confirming that the teacher has been successfully assigned to the course.

   - **View Course with Teacher Information**:
     - **Endpoint**: `/courses/{course_id}` (GET)
     - **Output**: JSON response including course details and the associated teacher's information (if available).

   - **Remove Teacher from Course**:
     - **Endpoint**: `/courses/{course_id}/remove-teacher` (DELETE)
     - **Output**: JSON response confirming that the teacher has been successfully removed from the course.

## Success Criteria
1. Admin is able to successfully assign a teacher to a course and receives confirmation in the response.
2. User is able to view the information of a course correctly along with the assigned teacher's details if available.
3. Admin is able to remove a teacher from a course successfully, which is reflected when fetching the course's details again.
4. The database migration completes without any disruption to existing Student, Course, and Teacher data.

## Key Entities
- **Course Table**:
  - **Updated Column**:
    - `teacher_id`: Integer (Foreign Key, references `Teacher.id`, can be null)

## Assumptions
- Admin users have the necessary permissions to assign and remove teachers from courses.
- The assigned teacher's ID must be valid and exist in the Teacher records.
- The existing tech stack is maintained throughout this feature development.

## Out of Scope
- Designing user interface components for assigning or viewing teacher-course relationships.
- Implementing features for notifications related to course assignments beyond basic record keeping.