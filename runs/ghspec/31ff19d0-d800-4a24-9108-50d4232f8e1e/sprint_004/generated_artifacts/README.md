# Updated README.md

# Student Management App

## Overview

The Student Management App allows for managing courses and student enrollments. Users can create courses, enroll students in courses, and retrieve information about enrolled courses.

## Database Schema

### Student-Course Junction Table

A new junction table `student_courses` has been added to manage the many-to-many relationship between `Student` and `Course`. The table encapsulates the following attributes:
- `id`: unique identifier (integer, primary key)
- `student_id`: foreign key referencing the `Student` table
- `course_id`: foreign key referencing the `Course` table

This structure allows for efficient enrollment management, enabling multiple students to enroll in a single course and a single student to enroll in multiple courses.

## API Endpoints

### Enroll Student in Course

- **Endpoint**: `POST /students/{studentId}/courses`
- **Request Body**:
    - `courseId`: integer (required)
- **Response**:
    - Returns a JSON object confirming the enrollment of the student in the given course, including both student and course details.

### Retrieve Student Enrolled Courses

- **Endpoint**: `GET /students/{studentId}/courses`
- **Response**:
    - Returns a JSON array containing all courses the specified student is enrolled in, detailing course attributes such as course name and level.

## Setup Instructions

To set up the database and run migrations, you need to execute the following commands:

1. Ensure you have appropriate database permissions.
2. Run the migration script to apply schema changes:
   ```bash
   python src/migrations.py
   ```

## Testing

Testing has been implemented to cover the following user scenarios:

1. **Enroll a Student in a Course**: A successful enrollment request is processed and returns the enrollment details.
2. **Retrieve a Student's Enrolled Courses**: Successfully retrieves a list of courses the student is enrolled in.
3. **Attempt to Enroll a Nonexistent Student**: An error is raised for invalid student identifiers.
4. **Attempt to Enroll a Student in a Nonexistent Course**: An error is raised for invalid course identifiers.

Tests are located in `tests/test_routes.py`. To run tests, execute:

```bash
pytest tests/
```

Make sure your test database is set up properly before running tests.