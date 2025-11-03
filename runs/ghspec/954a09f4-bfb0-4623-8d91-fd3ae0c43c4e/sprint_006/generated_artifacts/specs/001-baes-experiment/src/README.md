# README.md

# Educational Management System

## Overview

This project is a part of the Educational Management System, which manages courses, teachers, and students effectively.

## New Feature: Assign Teacher to Course

### API Endpoint

To assign a teacher to a course, use the following API endpoint:

**Endpoint**: `PATCH /courses/{course_id}/assign-teacher`

**Request Body**:

```json
{
  "teacher_id": "integer" (required)
}
```

- **Parameters**:
  - `teacher_id`: The ID of the teacher to be assigned to the course. This should be an integer corresponding to an existing teacher in the system.

### Success Response

On a successful assignment, the API will respond with a 200 OK status and a message indicating the operation succeeded:

**Response**:

```json
{
  "message": "Teacher assigned to course successfully.",
  "course": {
    "id": "integer",
    "teacher_id": "integer"
  }
}
```

- **Fields**:
  - `id`: The ID of the course to which the teacher has been assigned.
  - `teacher_id`: The ID of the teacher that has been assigned to the course.

### Error Responses

In the event that a teacher with the provided ID does not exist, the API will respond with a 404 Not Found error:

**Error Response**:

```json
{
  "error": {
    "code": "E002",
    "message": "Teacher not found."
  }
}
```

### Database Schema Update

To accommodate this new feature, the following changes have been made to the database schema:

- A new column, `teacher_id`, has been added to the `courses` table, which serves as a foreign key referencing the `teachers` table.

### Configurations Needed

Ensure your development environment is set up properly to handle this new feature:

1. **Setup Environment**:
   Make sure you're running the latest dependencies:
   ```bash
   pip install Flask SQLAlchemy Flask-Migrate
   ```

2. **Database Migration**:
   You will need to run the migration to update the database schema. Ensure you create a migration script similar to the following:

   ```python
   """Add teacher_id column to courses table"""
   from alembic import op
   import sqlalchemy as sa

   revision = 'xxxxxx'  # Update as necessary
   down_revision = 'previous_revision'

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
       op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

   def downgrade():
       op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
       op.drop_column('courses', 'teacher_id')
   ```

3. **Testing the API**:
   New test cases have been added to `tests/test_course_teacher.py` to validate the functionality.

By following these guidelines, developers can effectively implement and utilize the new feature to assign a teacher to a course within the Educational Management System.