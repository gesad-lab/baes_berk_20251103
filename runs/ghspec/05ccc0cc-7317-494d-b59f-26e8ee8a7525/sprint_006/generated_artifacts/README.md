# README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing Course entity and the newly introduced Teacher entity. This enhancement will enable the system to associate specific teachers with courses, thereby improving the administration of educational resources. By allowing a course to have an assigned teacher, we aim to provide better visibility into course management, facilitate teacher assignments, and streamline reporting on course-related activities.

## API Endpoints

### Assign a Teacher to a Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**:
  - `teacher_id` (integer, required): The ID of the teacher to be assigned to the course.
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body**:
    ```json
    {
      "message": "Teacher successfully assigned to the course."
    }
    ```

### Retrieve Course Details with Associated Teacher
- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
  - **Status Code**: 200 OK
  - **Body**:
    ```json
    {
      "course_id": 1,
      "course_name": "Mathematics 101",
      "teacher": {
        "teacher_id": 2,
        "teacher_name": "John Doe"
      }
    }
    ```

### Error Handling for Non-existent Teacher
- **Scenario**: A user attempts to assign a non-existent teacher to a course.
- **Response**:
  - **Status Code**: 404 Not Found
  - **Body**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Teacher does not exist."
      }
    }
    ```

## User Scenarios & Testing
1. **Assign a Teacher to a Course**:
   - **Scenario**: A user assigns a teacher to a course.
   - **Test**: Confirm that the system allows a teacher to be linked to a course successfully.

2. **Retrieve a Course with Teacher Details**:
   - **Scenario**: A user retrieves details of a specific course, including its assigned teacher.
   - **Test**: Verify that the API returns the course's information along with the teacher’s name.

3. **Error Handling for Non-existent Teacher**:
   - **Scenario**: A user attempts to assign a non-existent teacher to a course.
   - **Test**: Check that the API returns an appropriate error message indicating the teacher does not exist.

4. **Database Schema Migration**:
   - **Scenario**: Upon migration, the application starts without losing data in the existing Student, Course, or Teacher tables.
   - **Test**: Confirm that the database schema is updated to include a relationship while preserving existing records.

## Functional Requirements
This implementation will extend existing functionalities to:
- Introduce a `teacher_id` foreign key in the existing `Course` model.
- Provide API endpoints for assigning a teacher to a course and retrieving course details with associated teacher information.
- Ensure seamless database schema migration while maintaining existing records and integrity.