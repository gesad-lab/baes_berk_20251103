# File: docs/api_specifications.md

# API Specifications Documentation

## API Endpoints

### Course Management

#### Update Course Entity

- **Endpoint**: `/courses/{course_id}/assign-teacher`
- **Method**: `PATCH`
- **Description**: Assign a teacher to a specific course.

##### Request Body:
```json
{
  "teacher_id": "integer" (required)
}
```

##### Response:
- **Success (200 OK)**:
```json
{
  "message": "Teacher assigned to course successfully.",
  "course": {
    "id": "integer",
    "teacher_id": "integer"
  }
}
```
- **Error (404 Not Found)**:
```json
{
  "error": {
    "code": "E002",
    "message": "Teacher not found."
  }
}
```

### Database Schema Update

- **Course Table**: 
  - New column added:
    - `teacher_id`: Foreign key referencing the Teacher entity (integer, required)

### Migration Notes

- Ensure the migration for adding the `teacher_id` column preserves existing data for Student, Course, and Teacher entities without loss.
  
##### Migration Script Example:
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

## Success Criteria

- The API must allow a teacher to be assigned to a course with a success response containing the updated course details.
- Appropriate error messages must be displayed when trying to assign a non-existent teacher.
- Data integrity must be maintained for existing records following the database migration.