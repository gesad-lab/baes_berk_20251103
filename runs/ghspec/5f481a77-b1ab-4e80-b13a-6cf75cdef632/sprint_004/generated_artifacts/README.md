# README.md

# Student Management System

Welcome to the Student Management System project. This application manages courses and students, facilitating the association between them.

## Application Structure
```
student_management/
├── src/
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models (add StudentCourse relationship)
│   ├── schemas.py          # Marshmallow schemas for serialization (add StudentCourse schema)
│   ├── routes.py           # API routes for handling requests (add course relationship routes)
│   ├── config.py           # Configuration management
│   └── db.py               # Database initialization and schema handling
├── tests/
│   ├── test_routes.py      # Tests for API routes (add tests for relationships)
│   └── test_validation.py   # Tests for input validation (add tests for relationship validation)
├── .env.example             # Example environment configuration
└── README.md                # Project documentation
```

## API Endpoints

### Courses

- **POST /courses**
  - **Description**: Creates a new course with the provided data.
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
  - **Responses**:
    - **201 Created**: Returns the created course data.
      ```json
      {
        "id": 1,
        "name": "Introduction to Programming",
        "level": "Beginner"
      }
      ```
    - **400 Bad Request**: If the data is invalid, an error message is returned.
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Invalid course data"
        }
      }
      ```

### Students

- **POST /students**
  - **Description**: Creates a new student with the provided data.
  - **Request Body**:
    ```json
    {
      "first_name": "John",
      "last_name": "Doe"
    }
    ```
  - **Responses**:
    - **201 Created**: Returns the created student data.
      ```json
      {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe"
      }
      ```
    - **400 Bad Request**: If the data is invalid, an error message is returned.
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Invalid student data"
        }
      }
      ```

### Student-Course Relationship

- **POST /students/<student_id>/courses**
  - **Description**: Associate a student with a course.
  - **Request Body**:
    ```json
    {
      "course_id": 1
    }
    ```
  - **Responses**:
    - **200 OK**: Returns the updated student with the associated course.
      ```json
      {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "courses": [
          {
            "id": 1,
            "name": "Introduction to Programming"
          }
        ]
      }
      ```
    - **404 Not Found**: If the student or course does not exist.
      ```json
      {
        "error": {
          "code": "E003",
          "message": "Student or course not found"
        }
      }
      ```

## Testing

- To run the tests for the API, use the following command:
```bash
pytest tests/
```

Ensure that the environment is set up correctly as specified in the `.env.example` file.

## Environment Configuration

Copy `.env.example` to `.env` and fill in the required configuration values as per your environment.

## Conclusion

This README provides an overview of the Student Management System, detailing the core API functionalities and how to test them. Be sure to edit and build upon this document as the project evolves to maintain clarity for all contributors.