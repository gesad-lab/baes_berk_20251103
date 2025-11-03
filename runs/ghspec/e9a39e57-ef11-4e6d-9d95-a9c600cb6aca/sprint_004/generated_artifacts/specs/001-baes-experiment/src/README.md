# README.md

# Project Overview

This project is a Flask-based web application that allows students to enroll in courses, retrieve their course details, and remove themselves from courses. The application is built using SQLAlchemy for ORM and Alembic for database migrations.

## API Endpoints

### 1. Enroll Student in Course
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**: JSON containing the course ID (integer, required).
- **Response**: JSON confirmation with the student ID and course ID.

### 2. Retrieve Student Courses
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response**: JSON containing a list of course details (course ID, name, level) or an error message if the student is not found.

### 3. Remove Student from Course
- **Endpoint**: `DELETE /students/{student_id}/courses/{course_id}`
- **Response**: JSON confirmation of removal or an error message if the student or course does not exist.

## Database Setup and Migrations

### Database Schema Update
We have introduced a new junction table named `student_courses` to establish a many-to-many relationship between students and courses. The `student_courses` table has the following fields:

- `student_id`: Foreign key referencing the Student entity (integer, required).
- `course_id`: Foreign key referencing the Course entity (integer, required).

### Migration Script

Below is the migration script to create the `student_courses` table:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    op.drop_table('student_courses')
```

### Running Migrations
1. Ensure that Alembic is properly set up in your Flask application.
2. Run the migrations by executing the command:
   ```bash
   alembic upgrade head
   ```

### Important Notes
- The migration script must be executed to update the database schema before using the new enrollment features.
- This migration is designed to ensure that existing student and course data remain unaffected.

## Local Deployment
Ensure the application can run locally after the integration of course enrollment functionality. For more information on setup and requirements, refer to the `README.md` file at the root of the project.

## Future Enhancements
- Implement thorough error handling and validation for student and course ID inputs to ensure robustness.
- Expand the test coverage to include integration tests for the new student-course relationship functionalities.

---

This README provides a comprehensive guide regarding the new features added to the application and instructions on how to set up the database accordingly.