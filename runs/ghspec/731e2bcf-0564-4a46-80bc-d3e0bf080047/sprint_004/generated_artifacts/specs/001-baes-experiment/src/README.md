# README.md

## API Documentation

### New API Endpoints

#### Assign Courses to a Student

- **Endpoint**: `POST /students/{student_id}/courses`
- **Description**: This endpoint assigns courses to a specific student identified by `student_id`.
- **Request Body**:
  ```json
  {
    "course_ids": [1, 2, 3]  // Array of course IDs to be linked to the student
  }
  ```
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "message": "Courses assigned successfully.",
      "student": {
        "id": 1,
        "name": "John Doe",
        "courses": [1, 2, 3] // IDs of the assigned courses
      }
    }
    ```
  - **Error (400 Bad Request)**: If the student ID or course IDs are invalid.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid student ID or course IDs."
      }
    }
    ```

#### Retrieve a Student's Information with Courses

- **Endpoint**: `GET /students/{student_id}`
- **Description**: Retrieve details of the student identified by `student_id`, including the courses they are enrolled in.
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "courses": [
        {
          "id": 1,
          "title": "Mathematics"
        },
        {
          "id": 2,
          "title": "Science"
        }
      ]
    }
    ```
  - **No Courses Assigned (204 No Content)**: If the student is not enrolled in any courses.
  - **Error (404 Not Found)**: If the student ID does not exist.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

### Database Schema Update

#### Student Table Modification

- **Change**: A foreign key reference from the `Student` table to the `Course` table has been added.
- **Impact**: This allows establishing a one-to-many relationship, where each student can be enrolled in multiple courses.
- **Migration Details**: Ensure that existing data integrity is maintained during migration. The foreign key constraint guarantees that each referenced course ID corresponds to an existing record in the `Course` table.

### Assumptions

- The application is capable of handling schema migrations without data loss.
- Admin users have the rights to assign courses and access student records, ensuring that permissions are correctly managed.

### Future Considerations

- User interface changes for course assignment visualization will be considered in subsequent updates.
- The capability to remove courses from enrollment or enforce course prerequisites is outside the current scope and might be introduced in future versions.