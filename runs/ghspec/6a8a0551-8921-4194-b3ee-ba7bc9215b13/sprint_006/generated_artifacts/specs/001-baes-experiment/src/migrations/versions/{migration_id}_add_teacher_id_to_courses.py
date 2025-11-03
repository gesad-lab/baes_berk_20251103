```python
"""Add teacher_id to courses table

Revision ID: {migration_id}
Revises: PreviousMigrationID
Create Date: 2023-10-01 12:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '{migration_id}'
down_revision = 'PreviousMigrationID'
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add the teacher_id column to the courses table."""
    # Add the 'teacher_id' column as a foreign key referencing the 'teachers' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')


def downgrade():
    """Rollback the migration by removing the teacher_id column and foreign key constraint."""
    # Drop the foreign key constraint
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    # Remove the 'teacher_id' column
    op.drop_column('courses', 'teacher_id')
```