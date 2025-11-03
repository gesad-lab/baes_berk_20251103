# File: docs/api_reference.md

# API Reference Documentation

## Endpoints

### 1. Assign Teacher to Course
- **Endpoint**: `PUT /courses/{course_id}/assign-teacher`
- **Request Body**:
    - JSON object:
    ```json
    {
        "teacher_id": "teacher_id"
    }
    ```
- **Description**: Assign a Teacher to a Course by updating the Course with the Teacher's ID.
- **Response**:
    - **Success**:
        - Status: `200 OK`
        - JSON confirmation message:
        ```json
        {
            "message": "Teacher successfully assigned to the course."
        }
        ```
    - **Error**:
        - Status: `400 Bad Request`
        - JSON error message if the Teacher ID is invalid or missing:
        ```json
        {
            "error": {
                "code": "E001",
                "message": "Invalid Teacher ID provided."
            }
        }
        ```

### 2. Retrieve Course Information
- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
    - **Success**:
        - Status: `200 OK`
        - JSON object including Course details along with associated Teacher information (if assigned):
        ```json
        {
            "course_id": "course_id",
            "course_name": "Course Name",
            "teacher": {
                "teacher_id": "teacher_id",
                "teacher_name": "Teacher Name"
            }
        }
        ```
    - **Error**:
        - Status: `404 Not Found`
        - JSON error message if the Course does not exist:
        ```json
        {
            "error": {
                "code": "E002",
                "message": "Course not found."
            }
        }
        ```

### 3. Error Handling for Teacher Assignment
- **Scenario**: A user attempts to assign a Teacher to a Course without providing a valid Teacher ID.
- **Expected Outcome**: The API validates that appropriate error messages are returned if the Teacher ID is missing or invalid.

### 4. Database Migration
- **Modification**: Update the database schema to implement the relationship between Course and Teacher.
    - **Additional Column**: `teacher_id` (references `teachers.id`)
- **Testing**: Verify that existing data for Students, Courses, and Teachers remains accessible before and after the migration.

## Summary of Changes
- New endpoint for assigning a Teacher to a Course.
- Endpoint for retrieving Course information including associated Teacher details.
- Improved error handling for invalid Teacher assignments.
- Database schema update to maintain referential integrity between Courses and Teachers without losing existing data.