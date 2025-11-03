```python
"""Add course_ids column to students table.

Revision ID: 2023_10_16_000001
Revises: 
Create Date: 2023-10-16 00:00:00
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2023_10_16_000001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add course_ids column to the students table.

    This upgrade adds a new column 'course_ids' to the 'students' table,
    allowing for a one-to-many relationship between students and courses.
    
    The course_ids will be stored as a comma-separated string.
    
    Ensure there is no data loss during this migration.
    """
    with op.batch_alter_table('students') as batch_op:
        batch_op.add_column(sa.Column('course_ids', sa.Text(), nullable=True))


def downgrade() -> None:
    """Remove course_ids column from the students table.

    This downgrade reverts the upgrade by removing the 'course_ids' column
    from the 'students' table if it exists.
    """
    with op.batch_alter_table('students') as batch_op:
        batch_op.drop_column('course_ids')
```