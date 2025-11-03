```markdown
# README.md

# Student Management Web Application

This project provides a comprehensive backend for managing students and their enrollments in various courses. This documentation outlines the setup, usage, and newly introduced enrollment features.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student_management_app.git
   cd student_management_app
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ and then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**:
   Use the provided `.env.example` to create your `.env` file with the necessary environment variables.

4. **Run the Database Migrations**:
   Ensure your database is set up correctly and apply the migrations:
   ```bash
   alembic upgrade head
   ```

5. **Start the FastAPI Application**:
   You can start the application using:
   ```bash
   uvicorn src.main:app --reload
   ```

## Enrollment Feature

The enrollment feature allows students to be linked to courses. Below are the API endpoints and usage examples.

### API Endpoints

#### 1. Enroll a Student in a Course

- **Endpoint**: `POST /enrollments`
- **Request Body**:
  ```json
  {
    "student_id": "1",
    "course_id": "101"
  }
  ```
- **Success Response**:
  ```json
  {
    "id": "10",
    "student_id": "1",
    "course_id": "101"
  }
  ```
- **Error Responses**:
  - **400 Bad Request**: If `student_id` or `course_id` is missing or invalid.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Student ID and Course ID are required.",
        "details": {}
      }
    }
    ```

#### 2. Retrieve Enrolled Courses for a Student

- **Endpoint**: `GET /students/{student_id}/enrollments`
- **Path Parameter**: `student_id`
- **Success Response**:
  ```json
  [
    {
      "course_id": "101",
      "course_name": "Physics 101"
    },
    {
      "course_id": "102",
      "course_name": "Chemistry 101"
    }
  ]
  ```

### Notes

- Ensure that both Student ID and Course ID are valid and exist in the database before processing the enrollment.
- The database schema updates should preserve existing Student and Course data.

## Testing

To run the tests, make sure your test database is set up, and then use:
```bash
pytest
```

### Test Coverage Requirements

- Ensure at least 70% coverage for the business logic associated with the enrollment feature.
- Critical paths should maintain above 90% coverage.

## Conclusion

By establishing the enrollment feature, the Student Management Web Application can efficiently manage student enrollments across various courses, enhancing both administrative operations and educational tracking.
```