# src/database/migrations/README.md

# Migration for Teacher-Course Relationship

## Overview

This migration is designed to update the existing database schema to include a relationship between `Course` and `Teacher`. The migration will add a foreign key in the `Course` table referencing the `Teacher` entity, allowing for the assignment of teachers to courses. It is critical that this migration preserves all existing `Student`, `Course`, and `Teacher` data.

## Migration Details

To proceed with this migration, we'll be utilizing Alembic as our migration tool.

### 1. Create Migration Script

1. **Initialize Alembic (if not already done):**
   ```bash
   alembic init migrations
   ```

2. **Create Migration:**
   Run the following command to create a new migration script:
   ```bash
   alembic revision --autogenerate -m "Add teacher_id to Course table"
   ```

### 2. Modify the Migration Script

Ensure this migration script includes the following changes.

#### Add Foreign Key to Course Table

In the generated migration file located in the `migrations/versions` directory, make the following changes to include the `teacher_id` column with a foreign key constraint.

```python
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# Revision identifiers, used by Alembic.
revision = 'XXXXXXXXXX'  # Replace with the generated revision ID
down_revision = 'YYYYYYYYYY'  # Replace with the previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    # Add the teacher_id column to the Course table
    op.add_column('Course', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key relationship to Teacher table
    op.create_foreign_key('fk_teacher_course', 'Course', 'Teacher', ['teacher_id'], ['id'])

def downgrade():
    # Remove the foreign key constraint
    op.drop_constraint('fk_teacher_course', 'Course', type_='foreignkey')
    
    # Drop the teacher_id column
    op.drop_column('Course', 'teacher_id')
```

### 3. Run the Migration

After modifying the migration script, run the following command to apply the migration to your database:

```bash
alembic upgrade head
```

### 4. Testing the Migration

It’s essential to validate that the migration worked correctly and that existing data is intact. Once the migration has been applied, conduct the following tests:

- Confirm that the `teacher_id` column exists in the `Course` table.
- Ensure that existing records in the `Course`, `Student`, and `Teacher` tables remain unchanged.
- Write new unit and integration tests that cover the assignment of teachers to courses and retrieval of course details with teacher information.

### Conclusion

Following these steps will ensure that the database is correctly migrated to support assigning teachers to courses. This migration is crucial for the new functionality outlined in the project specifications, ensuring that all data integrity is maintained throughout the process.