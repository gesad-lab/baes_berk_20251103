```python
"""Add teacher_id to courses

Revision ID: c7c8f1edc8ab
Revises: xxx
Create Date: 2023-10-05 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from src.models import Course, Teacher  # Import models for reference


# revision identifiers, used by Alembic.
revision = 'c7c8f1edc8ab'
down_revision = 'xxx'  # Replace with the ID of your last migration
branch_labels = None
depends_on = None


def upgrade():
    """Apply the upgrade for adding teacher_id."""
    op.add_column('courses', sa.Column('teacher_id', sa.UUID(), sa.ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Apply the downgrade to remove teacher_id."""
    op.drop_column('courses', 'teacher_id')
```