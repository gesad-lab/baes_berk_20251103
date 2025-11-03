# README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the newly created Teacher entity. By adding this relationship, each course can have a designated teacher who is responsible for it. This enhancement will facilitate better organization of courses and improve educational management capabilities within the system.

## API Endpoints

### Assign a Teacher to a Course
- **Endpoint**: `/courses/{course_id}/assign-teacher`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "teacher_id": <Integer> // required
  }
  ```
- **Response**:
  - **Status**: 200 OK
  - **Content**:
  ```json
  {
    "message": "Teacher has been successfully assigned to the course."
  }
  ```

### View Course with Teacher Information
- **Endpoint**: `/courses/{course_id}`
- **Method**: GET
- **Response**:
  - **Status**: 200 OK
  - **Content**:
  ```json
  {
    "id": <Integer>,
    "name": "<Course Name>",
    "teacher": {
      "id": <Integer>,
      "name": "<Teacher Name>"
    }
  }
  ```

### Remove Teacher from Course
- **Endpoint**: `/courses/{course_id}/remove-teacher`
- **Method**: DELETE
- **Response**:
  - **Status**: 200 OK
  - **Content**:
  ```json
  {
    "message": "Teacher has been successfully removed from the course."
  }
  ```

## Database Migration
The migration process for updating the `Course` table to include the new `teacher_id` column will ensure that no existing data for Courses, Students, or Teachers is affected, preserving the integrity of the current records. The new column will allow for courses to have assigned teachers when appropriate.

## User Scenarios
1. **Assign a Teacher to a Course**:
   - As an admin, I want to assign a teacher to a specific course, so that I can manage which instructor is responsible for the course.

2. **View Course Details**:
   - As a user, I want to view the course details along with the assigned teacher's information, so that I can understand the course structure better.

3. **Remove a Teacher from a Course**:
   - As an admin, I want to unassign a teacher from a course, so that I can reassign teaching responsibilities as needed.