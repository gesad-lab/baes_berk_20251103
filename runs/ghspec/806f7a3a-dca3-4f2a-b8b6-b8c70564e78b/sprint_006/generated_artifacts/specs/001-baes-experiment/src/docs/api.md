# Updating API Documentation in `/docs/api.md`

# API Documentation

## Teacher and Course Management API

### Add Teacher to Course

- **Endpoint**: `/api/v1/courses/{course_id}/teachers`
- **Method**: POST
- **Description**: Allows an administrator to link a teacher to a course by updating the Course entity to include a teacher ID.
- **Request Body**:
  ```json
  {
      "teacher_id": "<integer>"
  }
  ```
- **Response**:
  - **200 OK**: Teacher successfully added to the course.
    ```json
    {
        "message": "Teacher assigned to course successfully."
    }
    ```
  - **400 Bad Request**: If the teacher ID does not correspond to an existing Teacher record.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid teacher ID provided."
        }
    }
    ```
  - **404 Not Found**: If the course does not exist.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

### Get Course Details

- **Endpoint**: `/api/v1/courses/{course_id}`
- **Method**: GET
- **Description**: Retrieves details for a specific course, including the related teacher’s name and email.
- **Response**:
  - **200 OK**: Returns course details including assigned teacher information.
    ```json
    {
        "course_id": "<integer>",
        "title": "<string>",
        "teacher": {
            "name": "<string>",
            "email": "<string>"
        }
    }
    ```
  - **404 Not Found**: If the course does not exist.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

### Database Notes
- The Course table has been updated to include a new column for the Teacher relationship:
  - **Column**: `teacher_id` (Integer, Foreign Key referencing `Teacher(id)`)

---

### Validation and Notes
- Validation checks are implemented to ensure that assigned teacher IDs exist within the Teacher entity before making an association.
- All responses are in JSON format, ensuring consistent and relatable data structures throughout the API.

---

This documentation reflects the latest updates of the API to facilitate the relationships between courses and teachers effectively.