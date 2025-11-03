```python
"""Add teacher_id to courses table

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
    """Add teacher_id column to the courses table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Remove teacher_id column from the courses table."""
    op.drop_column('courses', 'teacher_id')
```