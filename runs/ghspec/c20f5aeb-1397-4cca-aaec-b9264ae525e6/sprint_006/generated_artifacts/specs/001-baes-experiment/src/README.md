# README.md

# Student Management System

## API Documentation

### Course Entity Update

#### Course Entity
The `Course` entity has been updated to include a new field:
- `teacher_id`: Integer (foreign key referencing the `Teacher` entity)

### Assign Teacher to Course Endpoint

- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**: 
  ```json
  {
      "teacher_id": 1
  }
  ```
- **Response**:
  - **Success**: 
    ```json
    {
        "message": "Teacher assigned successfully."
    }
    ```
  - **Error**: 
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid teacher ID."
        }
    }
    ```

### Retrieve Course with Teacher Details Endpoint

- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
  ```json
  {
      "id": 1,
      "title": "Course Title",
      "description": "Course Description",
      "teacher": {
          "id": 1,
          "name": "Teacher Name",
          "email": "teacher@example.com"
      }
  }
  ```

### Database Schema Update

- The `Course` table has been updated to include a `teacher_id` field while ensuring that the addition does not disrupt existing records in the `Student`, `Course`, and `Teacher` tables.
- Migrations will maintain data integrity and ensure no data loss occurs during the update.

### Data Validation

- The `teacher_id` field is validated upon assignment to ensure it corresponds to a valid `Teacher` entity in the system. Validation errors will return a clear, actionable message.

---

For more information, visit the [Project Repository](link-to-repo).