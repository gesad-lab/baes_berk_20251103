# Feature: Add Teacher Relationship to Course Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the `Course` entity and the `Teacher` entity. By allowing each course to be associated with a teacher, we aim to enhance the course management capabilities within the educational management system. This will facilitate better oversight of course assignments and improve the overall educational experience for both students and educators.

## User Scenarios & Testing
1. **Scenario 1: Assign a Teacher to a Course**  
   - **Given**: An administrator has created a course and a teacher.  
   - **When**: The administrator assigns a teacher to the course.  
   - **Then**: The system should update the course entry to reflect the assigned teacher.

2. **Scenario 2: View Course with Assigned Teacher**  
   - **Given**: A course has an assigned teacher.  
   - **When**: The administrator requests to view the course details.  
   - **Then**: The system should return course information along with the teacher's details.

3. **Scenario 3: Attempt to Assign a Non-Existent Teacher**  
   - **Given**: An administrator attempts to assign a teacher that does not exist in the system.  
   - **When**: The administrator submits the assignment request.  
   - **Then**: The system should return an error message indicating the teacher is not found.

## Functional Requirements
1. **Course-Teacher Relationship**  
   - Update the `Course` entity to include a relationship (foreign key) to the `Teacher` entity.
     - New attribute in `Course`:
       - `teacher_id`: Integer (foreign key referencing `Teacher.id`, nullable)

2. **Database Schema Update**  
   - Modify the existing `Course` table to add the `teacher_id` field without affecting existing data in the `Student`, `Course`, and `Teacher` tables.

3. **API Endpoints**  
   - **PUT /courses/{courseId}/assign-teacher**: Accepts a JSON object to assign a teacher to an existing course.
     - Request Body: `{ "teacher_id": "integer" }`
     - Response Success: JSON message confirming the assignment.
     - Response Error: JSON error message if the teacher ID is invalid or does not exist.
   
   - **GET /courses/{courseId}**: Extended to include teacher information if assigned.
     - Response: `{ "id": "integer", "title": "string", "description": "string", "teacher": { "id": "integer", "name": "string" } }`

4. **Database Migration**  
   - Implement a migration to add the `teacher_id` column to the `Course` table without affecting existing data.

5. **Input Validation**  
   - Validate that the `teacher_id` exists in the database before assigning it to the course.
   - Ensure the course can only have a single teacher assigned.

## Success Criteria
- The application must return a status of 200 OK for successful teacher assignment, with a confirmation message.
- A course can be successfully updated to assign a valid teacher, and the teacher should be retrievable through the course detail endpoint.
- Attempts to assign a non-existent teacher must return an informative error message.
- The course details should accurately reflect the assigned teacher information in the JSON response.

## Key Entities
- **Course**
  - Attributes:
    - `id`: Integer (auto-generated ID)
    - `title`: String (not null)
    - `description`: String
    - `teacher_id`: Integer (nullable, foreign key referencing `Teacher.id`)

- **Teacher**
  - Attributes:
    - `id`: Integer (auto-generated ID)
    - `name`: String (not null)
    - `email`: String (not null, must be unique)

## Assumptions
- Administrators have the necessary permissions and access to assign teachers to courses.
- Teacher and Course data will be already present in the system prior to this feature implementation.
- The existing database supports adding foreign key relationships without compromising performance.

## Out of Scope
- The ability to remove or change the teacher assigned to a course.
- Front-end changes or UI components for the assignment of teachers to courses.
- Comprehensive logging or tracking of assignment changes for historical records.
- Handling scenarios where multiple teachers could be assigned to a single course in the future.