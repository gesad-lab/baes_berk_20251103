```python
"""Add teacher relationship to courses.

This migration script updates the existing courses table to include a 
nullable teacher_id foreign key referencing the id field of the teachers table,
establishing a one-to-many relationship where each course can be assigned one 
teacher, while a teacher can handle multiple courses.
"""

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '2023_10_01_add_teacher_relationship'
down_revision = None  # update this if there's a previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to add the teacher_id column to the courses table."""
    # Add the new column `teacher_id` as nullable
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create a foreign key constraint on the teacher_id column
    op.create_foreign_key(
        'fk_teacher_id',  # Name of the foreign key constraint
        'courses',        # Source table
        'teachers',       # Referenced table
        ['teacher_id'],   # Source column
        ['id'],           # Referenced column
        ondelete='SET NULL'  # Set the teacher_id to NULL if the referenced teacher is deleted
    )

def downgrade():
    """Revert the migration by removing the teacher_id column from the courses table."""
    # Drop foreign key constraint first to remove the column safely
    op.drop_constraint('fk_teacher_id', 'courses', type_='foreignkey')
    
    # Remove the `teacher_id` column
    op.drop_column('courses', 'teacher_id')
```