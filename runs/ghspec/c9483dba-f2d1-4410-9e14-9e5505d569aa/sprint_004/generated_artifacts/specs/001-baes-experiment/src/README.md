# README.md

# Student Management System

## Overview
This application provides functionality for managing students and their corresponding courses. The application allows users to assign courses to students and retrieve student details along with their enrolled courses.

## User Scenarios
1. **Assign Course to Student**: 
   - Users can assign a specific course to a student by sending a request with the student ID and course ID.
   - The system responds with the updated student details including their associated courses.

2. **Retrieve Student with Courses**: 
   - Users can request details of a specific student by ID, including all courses they are enrolled in.
   - The system responds with the student's details in JSON format, along with a list of their courses.

## Functional Requirements

### Assign Course to Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Input**: 
  - JSON payload containing the following fields:
    - `course_id`: String (required)
- **Output**: 
  - JSON response containing the updated Student's ID and a list of their courses.

### Retrieve Student with Courses
- **Endpoint**: `GET /students/{id}`
- **Input**: 
  - Student ID in the URL path.
- **Output**: 
  - JSON response containing the Student's ID, name, email, and a list of courses they are enrolled in.

## Validation Scenarios
- If a course is assigned to a non-existent student, the application responds with an error indicating that the student ID is invalid (Error code: E002).
- If a user attempts to retrieve a student with an invalid ID, the application responds with an error indicating that the student is not found.

## Database Management
- The existing `Student` table has been updated to include a many-to-many relationship with the `Course` table.
- Any migration scripts must maintain the integrity of existing Student and Course data during this schema update.

## Migration
- Migration scripts are located in the `migrations/` directory, managed using Flask-Migrate.
- To apply migrations, use the following commands:
  ```bash
  flask db migrate -m "Add many-to-many relationship between Students and Courses"
  flask db upgrade
  ```

## Setup
Ensure that you have [Flask](https://flask.palletsprojects.com/) and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) installed in your Python environment. You can install them via pip:
```bash
pip install Flask Flask-Migrate
```

## Running the Application
To run the application, execute:
```bash
flask run
```

## Testing
To run the test suite, use:
```bash
pytest
```

Make sure to add tests for new functionalities as they are implemented to ensure full coverage and maintainability.

## Contribution
Contributions are welcome! Please follow the existing patterns and guidelines while making changes.