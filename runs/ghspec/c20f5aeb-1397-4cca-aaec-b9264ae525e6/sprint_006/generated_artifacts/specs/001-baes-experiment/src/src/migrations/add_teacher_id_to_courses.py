```python
"""Add teacher_id to courses

Revision ID: abc123def456
Revises: previous_revision_id
Create Date: 2023-10-10 12:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abc123def456'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade the database schema by adding teacher_id to the courses table."""
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Create foreign key constraint linking teacher_id to the teachers table
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'], ondelete='SET NULL')


def downgrade():
    """Downgrade the database schema by removing teacher_id from the courses table."""
    # Drop the foreign key constraint first
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    
    # Remove the teacher_id column from the courses table
    op.drop_column('courses', 'teacher_id')
```