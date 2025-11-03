```python
"""008_add_teacher_relationship_to_courses.py

Alembic migration script to add a teacher_id column to the courses table.
This new column will serve as a foreign key referencing the id field in 
the teachers table, establishing a relationship between courses and teachers.
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '008_add_teacher_relationship_to_courses'
down_revision = '007_previous_migration'  # Update with the last migration identifier
branch_labels = None
depends_on = None

def upgrade():
    """Add teacher_id column to the courses table as a foreign key referencing the teachers table."""
    # Adding the new column `teacher_id` to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Creating a foreign key relationship with the teachers table
    op.create_foreign_key(
        'fk_teacher_course',  # Constraint name
        'courses',  # Source table
        'teachers',  # Target table
        ['teacher_id'],  # Source columns
        ['id'],  # Target columns
        ondelete='SET NULL'  # Set to NULL if the referenced teacher is deleted
    )

def downgrade():
    """Remove teacher_id column from the courses table."""
    # Dropping the foreign key constraint
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')

    # Dropping the `teacher_id` column
    op.drop_column('courses', 'teacher_id')
```