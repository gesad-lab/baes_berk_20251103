```python
"""Add Teacher Relationship to Course

Revision ID: xxxxxx
Revises: previous_revision_id
Create Date: 2023-10-10 18:00:00.000000

"""

from alembic import op
import sqlalchemy as sa
from src.models import Course  # Adjust this import based on your actual project structure

# revision identifiers, used by Alembic.
revision = 'xxxxxx'
down_revision = 'previous_revision_id'  # Update with the actual previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Add the teacher_id column to the Course table."""
    op.add_column('course', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_teacher_course',
        'course',
        'teacher',
        ['teacher_id'],
        ['id'],
        ondelete='SET NULL'  # Set to NULL if the referenced teacher is deleted
    )

def downgrade():
    """Remove the teacher_id column from the Course table."""
    op.drop_constraint('fk_teacher_course', 'course', type_='foreignkey')
    op.drop_column('course', 'teacher_id')
```