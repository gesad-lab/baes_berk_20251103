# README.md

# Project Title

## Setup Instructions

### 1. Set Up Environment

1. Ensure that you have Python installed on your system. It is recommended to use Python 3.8 or later.
2. Create and activate a virtual environment. You can use the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the necessary dependencies by running:

   ```bash
   pip install Flask SQLAlchemy Marshmallow pytest alembic
   ```

### 2. Database Schema Migration

To create the necessary database schema, you will need to use Alembic for handling migrations:

1. Navigate to your project directory and initialize Alembic:

   ```bash
   alembic init alembic
   ```

2. Update your Alembic configuration to reflect your database URI.

3. Create a migration script that adds a `teacher_id` foreign key to the `courses` table while ensuring existing relationships in the database are preserved. Here is an example script:

   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
       op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', 'teacher_id', 'id')

   def downgrade():
       op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
       op.drop_column('courses', 'teacher_id')
   ```

4. Run the migration:

   ```bash
   alembic upgrade head
   ```

### 3. API Development

1. You can implement APIs such as `/courses/{courseId}/assign-teacher` to assign a teacher to a course. Ensure you validate both IDs and handle error scenarios gracefully.
2. Use Marshmallow for schema validation and serialization when assigning teachers.

### 4. Testing

1. Make sure to have unit tests and integration tests in place. The target coverage for business logic is a minimum of 70%, and 90% for validation.
2. Test scenarios should include valid assignments, retrievals, and error handling for invalid IDs.

### 5. Documentation

Update your API documentation to reflect any new endpoints and provide usage examples in this README as needed.

---

For further details about usage and functionalities, please refer to the [Implementation Plan](implementation_plan_add_teacher_relationship_to_course_entity.md).