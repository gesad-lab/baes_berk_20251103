# README.md

# Student Management API

This project provides a RESTful API for managing students, courses, and teachers in an educational context. Built using FastAPI and SQLite, it allows for the efficient management of resources.

## API Endpoints

### Courses

#### Assign a Teacher to a Course

- `POST /courses/{course_id}/assign-teacher`
  
  Assign a teacher to a specified course. The request requires a JSON body with the `teacher_id`.

  **Request Body Example**:
  ```json
  {
    "teacher_id": 123
  }
  ```

  **Responses**:
  - **200 OK**: Teacher assigned successfully.
  - **400 Bad Request**: Invalid request body.
  - **404 Not Found**: Course not found.

#### Retrieve Course Information

- `GET /courses/{course_id}`
  
  Retrieve information for a specific course, including the associated teacher’s name if assigned.

  **Responses**:
  - **200 OK**: Successful retrieval of course information.
    - Response format:
    ```json
    {
      "course_id": 1,
      "course_name": "Math 101",
      "teacher": {
        "id": 123,
        "name": "Jane Doe"
      }
    }
    ```
  - **404 Not Found**: Course not found.

## Database Changes

### Course Model Update

- The Course database schema has been updated to include a `teacher_id` column that references the Teacher's `id`. This ensures a foreign key relationship between courses and teachers.

### Migration

- The migration process integrates the new `teacher_id` column into the existing Course table without affecting existing data for Students, Courses, or Teachers.

## Testing

New tests have been added for the `/courses/{course_id}/assign-teacher` endpoint in the `tests/test_courses.py` file, ensuring that the functionality works as expected.