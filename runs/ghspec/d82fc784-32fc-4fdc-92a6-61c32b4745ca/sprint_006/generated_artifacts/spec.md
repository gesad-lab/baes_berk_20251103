# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course and Teacher entities. This relationship will allow each Course to be associated with a specific Teacher, enhancing the system's ability to manage course assignments and teacher responsibilities effectively. This improvement is designed to streamline course management processes and better facilitate communication between students and their teacher.

## User Scenarios & Testing
1. **As a user, I want to assign a teacher to a course** so that the course has a designated educator.
   - Test: Update an existing course to include a teacher ID and verify that the course record now reflects the assigned teacher.

2. **As a user, I want to retrieve a course along with its associated teacher** to get a complete view of the course details.
   - Test: Send a GET request for a specific course and confirm that the response includes the teacher's details alongside the course information.

3. **As a user, I want to ensure that courses without assigned teachers are still retrievable** to enable course management continuity.
   - Test: Fetch a list of courses, ensuring that courses without assigned teachers are included in the response without causing errors.

4. **As a user, I want to confirm that updating a course's teacher details does not affect other course or teacher information** so that data integrity is maintained.
   - Test: Update the teacher associated with a course and verify that changes reflect accurately without impacting unrelated records.

5. **As a user, I want to ensure that existing Student, Course, and Teacher data persists and is intact** during the database migration process.
   - Test: Check the integrity and availability of existing records in the Student, Course, and Teacher tables after the migration.

## Functional Requirements
1. **Add Teacher Relationship to Course**:
   - Modify the Course entity to include a new field:
     - `teacher_id`: Integer (Foreign Key referencing the Teacher entity, which must allow null values to support courses without an assigned teacher).

2. **Update Existing Course**:
   - API Endpoint: PATCH `/courses/{course_id}`
   - Request Body: JSON containing `{"teacher_id": 1}` (where 1 is the ID of the teacher to be assigned).
   - Success Response: HTTP Status 200 OK with the updated course record including the teacher ID.

3. **Retrieve Course with Teacher**:
   - API Endpoint: GET `/courses/{course_id}`
   - Success Response: HTTP Status 200 OK with JSON containing the course information including related teacher details if available.

4. **Database Schema Update**:
   - Modify the existing `courses` table to add the `teacher_id` column. 
     - `teacher_id`: Integer (nullable, Foreign Key)

5. **Database Migration**:
   - Create a migration that updates the `courses` schema to include the new `teacher_id` field, ensuring that this addition does not disturb existing Student, Course, or Teacher data.

## Success Criteria
- The application must properly assign teachers to courses and return the updated course records as specified.
- The newly added `teacher_id` field should be correctly integrated in the `courses` table.
- API endpoints must return appropriate HTTP status codes for all requests.
- Courses must correctly display teacher information when retrieved.
- Existing Student and Course records should remain unaffected by the schema changes.

## Key Entities
- **Course Entity**:
  - Fields:
    - `id`: Integer (Primary Key, required)
    - `title`: String (required)
    - `description`: String (optional)
    - `teacher_id`: Integer (nullable, Foreign Key referencing Teacher)

- **Teacher Entity**:
  - Fields:
    - `id`: Integer (Primary Key, required)
    - `name`: String (required)
    - `email`: String (required, unique)

## Assumptions
- Courses may exist without an assigned teacher to account for any unassigned or unallocated courses.
- Teacher IDs will be valid integers and existing Teachers will not be deleted while assignments are in effect.
- Existing data integrity for Students, Courses, and Teachers is supported by the migration process.

## Out of Scope
- User interface updates for course management that reflect these changes.
- Business logic related to the assignment process beyond simple relational linking.
- Notifications or alerts for course teacher assignments or updates.
- Changes to how courses and teacher assignments are visually represented to users.

---

This document outlines the necessary adjustments to link the Course entity with the Teacher entity within the existing educational system. This enhancement accommodates the incremental development context, ensuring previous functionalities remain preserved while enriching the capability of course management.