# README.md

# Student Management Application

This application provides functionalities for managing students, courses, and teachers. It includes features to assign teachers to courses and retrieve course details along with teacher information. 

## API Endpoints

### Assigning a Teacher to a Course

**Endpoint**: `PATCH /courses/{course_id}`  
**Description**: This endpoint allows the user to assign a teacher to a specific course.

**Request Body**:
```json
{
  "teacher_id": "string"
}
```
- `teacher_id`: The ID of the teacher to be assigned to the course. This must reference an existing teacher.

**Responses**:
- `204 No Content`: Successfully assigned the teacher to the course.
- `400 Bad Request`: If the provided `teacher_id` does not reference an existing teacher, an error message will be returned. Example:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Invalid teacher_id: Teacher does not exist."
    }
  }
  ```

### Retrieving Course Details with Teacher Information

**Endpoint**: `GET /courses/{course_id}`  
**Description**: This endpoint retrieves the details of a specific course, along with the information of the assigned teacher if available.

**Responses**:
- `200 OK`: Returns the course details including the teacher information. Example:
  ```json
  {
    "course_id": "string",
    "course_name": "string",
    "teacher": {
      "teacher_id": "string",
      "name": "string"
    }
  }
  ```
- `404 Not Found`: If the course with the specified ID does not exist. Example:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Course not found."
    }
  }
  ```

## Error Handling for Teacher-Course Relationship

- If a user attempts to assign a non-existent teacher to a course or if the course data is invalid, the application returns a `400 Bad Request` error with clear messaging, such as:
  ```json
  {
    "error": {
      "code": "E003",
      "message": "The course data is invalid."
    }
  }
  ```

## Database Migration

The database schema has been adjusted to include a `teacher_id` field in the Course entity, which establishes a relationship between courses and teachers, ensuring referential integrity.

## Testing

Automated tests have been implemented to cover the new feature, including validation scenarios for teacher assignments. Make sure to run the test suite to ensure all functionalities are working correctly.