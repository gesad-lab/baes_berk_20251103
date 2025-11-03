# README.md

# Project Title

## Overview
The purpose of this project is to establish a relationship between the existing `Course` and `Teacher` entities in the educational system. This relationship will allow each `Course` to be associated with a `Teacher`, facilitating improved course management and enhancing the educational experience by enabling better visibility of teaching staff associated with each course. This will streamline administrative processes and provide students with clear information about their instructors.

## Functional Requirements

1. **Assign Teacher to Course Endpoint**:
   - **HTTP method**: PATCH
   - **Endpoint**: `/courses/{courseId}/assign-teacher`
   - **Request body**:
     - `teacherId`: integer (required)
   - **Response**:
     - On success (HTTP 200):
       - JSON object confirming the teacher has been assigned.
     - On failure (HTTP 400):
       - JSON object with error message if the teacher does not exist or course ID is invalid.

2. **Retrieve Course Details with Teacher**:
   - **HTTP method**: GET
   - **Endpoint**: `/courses/{courseId}`
   - **Response**:
     - On success (HTTP 200):
       - JSON object containing:
         - `courseId`: integer
         - `courseName`: string
         - `level`: string
         - `teacher`: 
           - `id`: integer
           - `name`: string
           - `email`: string
     - On failure (HTTP 404):
       - JSON object with error message if the course does not exist.

3. **Database Migration**:
   - Update the `Course` entity schema to include a foreign key relationship to the `Teacher` entity.
   - Ensure that the migration process preserves existing data in the `Student`, `Course`, and `Teacher` entities.

## Migration Strategy

A new migration file will be created following Alembic's pattern to add the `teacherId` column to the existing `courses` table while ensuring data integrity:

```python
def upgrade():
    """Apply the migration to add teacherId foreign key to courses."""
    op.add_column('courses', sa.Column('teacherId', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    """Revert the migration by dropping teacherId."""
    op.drop_column('courses', 'teacherId')
```

## Assumptions
1. Admin users have the necessary permissions to assign teachers to courses.
2. Course and Teacher IDs provided during API requests are valid and correspond to existing records in the database.
3. The changes to the database schema will be backward compatible, ensuring existing data integrity and functionality.

## Module Boundaries
- **controllers**: Extend `course_controller.py` to handle the new endpoints for assigning teachers to courses.
- **models**: Update `models.py` to include `teacherId` in the `Course` entity and establish a relationship with the `Teacher` entity.
- **services**: Extend existing `course_service.py` for business logic related to assigning teachers to courses.
- **database**: Implement database migrations to alter the `Course` entity schema while preserving data integrity.

## Testing
- Ensure that all new functionalities are covered with unit tests in `tests/test_course.py` and integration tests in `tests/test_course_integration.py`.

## Additional Information
Keep the README updated with any future changes to the application structure or API endpoints, ensuring clarity for all developers involved in the project.