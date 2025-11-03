```python
"""Migration script to add `teacher_id` column to the `courses` table."""

from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'add_teacher_id_to_courses'
down_revision = None  # Replace with the last migration revision if applicable
branch_labels = None
depends_on = None


def upgrade():
    """Add `teacher_id` column to `courses` table."""
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade():
    """Remove `teacher_id` column from `courses` table."""
    op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```