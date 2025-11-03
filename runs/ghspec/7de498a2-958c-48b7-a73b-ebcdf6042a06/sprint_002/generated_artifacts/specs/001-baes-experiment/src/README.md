# README.md

# Project Title

This project implements a simple API to manage student records.

## API Endpoints

### 1. Create Student
- **Endpoint**: `POST /students`
- **Request Body**: 
  - `name`: a string representing the student's name (required)
  - `email`: a string representing the student's email address (required, must be a valid email format)
- **Response**: 
  - 201 Created with JSON representation of the new Student object including the email.

### 2. Retrieve Student
- **Endpoint**: `GET /students/{student_id}`
- **Response**: 
  - 200 OK with JSON representation of the Student, including the email if found.
  - 404 Not Found if the Student ID does not exist.

### 3. Update Student
- **Endpoint**: `PUT /students/{student_id}`
- **Request Body**:
  - `name`: a string representing the student's updated name (required)
  - `email`: a string representing the updated email address (required, must be a valid email format)
- **Response**:
  - 200 OK with JSON representation of the updated Student object, including the email.
  - 404 Not Found if the Student ID does not exist.

## Database Migration

### Overview
To properly manage the addition of the new `email` field to the existing `students` table without losing existing student data, a migration script will be used.

### Migration Script
To alter the existing database schema for the `students` table, the following Alembic migration script can be used:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add the email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    # Remove the email column if the migration is rolled back
    op.drop_column('students', 'email')
```

### Instructions for Running Migrations
1. Ensure Alembic is installed and configured in your project.
2. Run the following command to apply the migration:
   ```bash
   alembic upgrade head
   ```
3. To rollback the migration if needed, run:
   ```bash
   alembic downgrade -1
   ```

### Testing Migrations
Before deploying to production, always test your migration scripts on a staging environment to ensure:
- The `email` field is correctly added.
- Existing student entries without an email do not cause errors.

### Deployment Considerations
- The addition of the email field must remain backward compatible; existing student entries without email will not cause system errors.
- Document any configuration specific to your deployment environment in a `.env` file.

## Docker Setup
Ensure the new migration is included when containers are built and run. No additional changes are needed to the existing Docker setup.

## Conclusion
This README provides an overview of how to set up and run the migration for the student API. Please ensure to follow the instructions carefully to maintain the integrity of your database.