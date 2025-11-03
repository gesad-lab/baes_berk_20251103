# README.md

# Student Management System

This project provides a simple API for managing students and courses, allowing for student enrollment and course retrieval.

## Running Tests and Ensuring Coverage

To ensure that the application meets quality and coverage requirements, you can run all tests and verify the coverage.

### Pre-requisites

Ensure that you have the following installed on your system:
- Python 3.x
- Pip
- pytest
- pytest-cov

### Setup

1. Install the required packages.
   ```bash
   pip install -r requirements.txt
   ```

2. Run database migrations to set up the schema.
   ```bash
   alembic upgrade head
   ```

### Running Tests

To execute all tests and check the coverage, use the following command:

```bash
pytest --cov=src --cov-report=term-missing
```

### Coverage Requirements

The tests should cover the following functionalities:

- **Enrollment of a student in a course**: The application can successfully enroll a student and return a confirmation message.
- **Retrieval of courses linked to a specific student**: The application can retrieve all courses associated with a specific student and return accurate details.
- **Database schema functionality**: The database schema modifications support students being associated with multiple courses without data loss.
- **Automated tests**: All functionality must pass automated tests covering both the enrollment process and retrieval of course data.

### Example Endpoints

- **Enroll a student in a course**:
  - **POST /api/v1/enroll**
    - Request Body: 
      ```json
      {
          "student_id": 1,
          "course_id": 1
      }
      ```
    - Response: 
      ```json
      {
          "message": "Student enrolled in course successfully"
      }
      ```

- **Retrieve courses for a student**:
  - **GET /api/v1/students/{student_id}/courses**
    - Response: 
      ```json
      {
          "courses": [
              {
                  "id": 1,
                  "name": "Introduction to Programming",
                  "level": "Beginner"
              },
              ...
          ]
      }
      ```

### Notes

Make sure to maintain the codebase and update the tests as new features are added to ensure consistent coverage and functionality.