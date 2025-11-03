# README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Course entity and the newly introduced Teacher entity within the existing educational system. This relationship is vital for assigning specific teachers to courses, thereby enhancing the management of educational resources and improving the overall functionality of the application. By linking teachers to courses, we can facilitate better tracking of teaching assignments and performance, contributing to a more effective educational experience.

## API Endpoints

### Assign Teacher to Course
- **Endpoint**: `PUT /courses/{course_id}/assign-teacher`
- **Request Body**:
  ```json
  {
    "teacher_id": "string"  // Required: must be a valid Teacher identifier.
  }
  ```
- **Response**: 
  - Success message along with the updated Course object, including Teacher assignment details.
  
  ```json
  {
    "message": "Teacher assigned successfully",
    "course": {
      "id": "course_id",
      "name": "Course Name",
      "teacher": {
        "id": "teacher_id",
        "name": "Teacher Name",
        "email": "teacher@example.com"
      }
    }
  }
  ```

### Retrieve Course Details
- **Endpoint**: `GET /courses/{course_id}`
- **Response**: 
  - A JSON object containing the Course's details, including the assigned Teacher's name and email.
  
  ```json
  {
    "id": "course_id",
    "name": "Course Name",
    "teacher": {
      "name": "Teacher Name",
      "email": "teacher@example.com"
    }
  }
  ```

## Database Schema Update
- The database schema must be updated to include a foreign key relationship:
  - Add a `teacher_id` column to the existing Course table that references the Teacher entity.
  - Ensure that existing data in the course and teacher tables remains intact and consistent through the migration process.

## User Scenarios & Testing
1. **Assigning a Teacher to a Course**:
   - A user selects an existing Course and assigns a Teacher to it through the application interface.
   - Expected outcome: The system should successfully update the Course record with the assigned Teacher, and the user receives a confirmation message.

2. **Retrieving Course Details**:
   - A user requests to retrieve details of a specific Course, including its assigned Teacher.
   - Expected outcome: The system should return the Course details along with the Teacher's information.

## High-Level Architecture
- **Frontend**: Vanilla JavaScript for API interactions (using Fetch API), with forms designed to manage Course and Teacher assignments.
- **Backend**: Python Flask application to handle API requests related to Course and Teacher entities.
- **Database**: SQLite to manage data persistence, modifying the existing Course table to include a foreign key to the Teacher table.

## Testing
Make sure to run tests after updating the database schema and implementing the API endpoints to ensure everything works as expected.