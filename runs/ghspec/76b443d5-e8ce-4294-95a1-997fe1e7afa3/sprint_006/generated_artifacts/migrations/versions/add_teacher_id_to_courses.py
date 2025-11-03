```python
"""add_teacher_id_to_courses

Revision ID: xxx
Revises: previous_revision_id
Create Date: 2023-XX-XX XX:XX:XX.XXXXXX

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'xxx'  # Update with actual revision ID
down_revision = 'previous_revision_id'  # Update with the actual previous revision ID
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration by adding a new column to the Course table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Revert the migration by removing the teacher_id column from the Course table."""
    op.drop_column('courses', 'teacher_id')
```