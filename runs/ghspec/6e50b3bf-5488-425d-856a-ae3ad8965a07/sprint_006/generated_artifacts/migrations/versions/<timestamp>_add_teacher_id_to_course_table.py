```python
"""Add teacher_id to Course table

Revision ID: <timestamp>
Revises: <previous_revision_id>
Create Date: <timestamp>

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add the teacher_id column to the Course table."""
    # Add the teacher_id column as an integer, allowing NULL values
    op.add_column('course', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Create a foreign key relationship linked to the teacher_id in the Teacher table
    op.create_foreign_key(
        'fk_course_teacher',   # Name of the foreign key constraint
        'course',              # Source table
        'teacher',             # Target table
        ['teacher_id'],        # Source column
        ['teacher_id'],        # Target column
        ondelete='SET NULL'    # Action when a referenced row is deleted
    )


def downgrade():
    """Reverse the migration by removing the teacher_id column from the Course table."""
    # Drop the foreign key constraint
    op.drop_constraint('fk_course_teacher', 'course', type_='foreignkey')
    
    # Remove the teacher_id column
    op.drop_column('course', 'teacher_id')
```