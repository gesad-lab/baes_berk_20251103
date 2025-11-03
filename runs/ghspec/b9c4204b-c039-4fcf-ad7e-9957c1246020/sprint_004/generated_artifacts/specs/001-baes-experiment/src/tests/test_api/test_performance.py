```markdown
# API Specifications

## Enroll Student in Course
- **Endpoint**: `POST /enroll`
- **Request Body**:
  ```json
  {
      "student_id": 1,
      "course_id": 2
  }
  ```
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "status": "enrolled",
        "student_id": 1,
        "course_id": 2
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course ID is required"
        }
    }
    ```

## List Student Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response**:
  - **Success (200 OK)**:
    ```json
    [
        {
            "course_name": "Mathematics",
            "level": "Intermediate"
        },
        {
            "course_name": "Science",
            "level": "Beginner"
        }
    ]
    ```

## Database Schema Update
- A Many-to-Many relationship between `Students` and `Courses` will be established by creating a join table `student_courses` with the following schema:
  ```sql
  CREATE TABLE student_courses (
      student_id INTEGER,
      course_id INTEGER,
      PRIMARY KEY (student_id, course_id),
      FOREIGN KEY (student_id) REFERENCES students(id),
      FOREIGN KEY (course_id) REFERENCES courses(id)
  );
  ```

## JSON Responses
All API responses will be formatted as valid JSON.
```