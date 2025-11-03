# README.md

# Project Title

## Introduction

This API allows users to manage student enrollments in various courses effectively.

## Functional Requirements

### 1. Enroll Student in Course
- **Endpoint**: `POST /students/{student_id}/enroll`
  
- **Input**: A JSON object containing the following field:
  - `course_id`: (string) The ID of the Course to enroll the Student in.

- **Output**: A JSON response confirming the Student's enrollment in the Course:
  ```json
  {
    "message": "Enrollment successful",
    "student_id": "12345",
    "course_id": "67890"
  }
  ```

### 2. Retrieve Student's Enrolled Courses
- **Endpoint**: `GET /students/{student_id}/courses`

- **Output**: A JSON array containing all Courses the Student is enrolled in. Each Course object includes:
  - `id`: (string) The unique identifier of the course.
  - `name`: (string) The name of the course.
  - `level`: (string) The level of the course.

Example Response:
```json
[
  {
    "id": "67890",
    "name": "Introduction to Programming",
    "level": "Beginner"
  },
  {
    "id": "12345",
    "name": "Advanced Mathematics",
    "level": "Intermediate"
  }
]
```

### 3. Database Schema Update
- On application startup, the database schema must be updated to include a new junction table called `student_courses` that references the `Student` and `Course` tables. The table should have the following structure:
  - **Columns**:
    - `student_id`: Foreign key referencing the Student entity (non-null).
    - `course_id`: Foreign key referencing the Course entity (non-null).
  
  The migration must ensure that existing Student and Course data remains intact and correctly associated post-migration.

## Success Criteria
1. The application must respond with a `201` status code and a confirmation message including Student ID and Course ID upon successful enrollment.
2. The application must respond with a `200` status code and a JSON array of Course details when retrieving a Student's enrolled Courses.
3. The application should validate input and respond with a `400` status code and an appropriate error message when an invalid enrollment request (e.g., non-existent course) is made.
4. The database must be updated on startup with the new schema reflecting the `student_courses` table, without affecting existing Student or Course data.

## Out of Scope
- User interface for managing course enrollments; the focus is on the backend API.
- Additional features, such as managing enrollment statuses or prerequisites for Courses.
- The ability to unenroll Students from Courses.

## Initial Setup
1. **Database Migration**:
   - Use Alembic to create a migration script that adds the `student_courses` junction table to the existing database schema without disrupting existing data.
   
   Migration Script Example:
   ```python
   from alembic import op
   from sqlalchemy import Column, ForeignKey

   def upgrade():
       op.create_table(
           'student_courses',
           Column('student_id', ForeignKey('students.id'), nullable=False),
           Column('course_id', ForeignKey('courses.id'), nullable=False),
           primary_key=['student_id', 'course_id']
       )

   def downgrade():
       op.drop_table('student_courses')
   ```

2. **Environment Setup**:
   - Ensure the development environment is prepared for migration and API setup.

3. **Directory Structure**: No significant structural changes will be required; however, related files will be updated to handle the new course enrollment functionality.

## Scalability, Security, and Maintainability
- **Scalability**: The design supports future modifications or feature extensions, ensuring the framework can adapt without significant rework.
- **Security**: Input validation mechanisms are implemented to avert malicious attempts at SQL injection or data corruption.
- **Maintainability**: By adhering to established coding principles and structuring the application based on modules, ease of updates and future enhancements is ensured.

## API Reference
For detailed API usage, please refer to the individual endpoint sections above.