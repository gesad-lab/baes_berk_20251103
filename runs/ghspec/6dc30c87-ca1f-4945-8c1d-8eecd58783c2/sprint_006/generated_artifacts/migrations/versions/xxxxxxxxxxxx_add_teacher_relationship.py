```python
"""Add teacher relationship to courses

Revision ID: xxxxxxxxxxxx
Revises: 123456789abc
Create Date: 2023-10-02 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxxxxxxx'
down_revision = '123456789abc'
branch_labels = None
depends_on = None


def upgrade():
    """Add the teacher_id foreign key to the courses table."""
    # Adding a foreign key column `teacher_id` to the `courses` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_teacher_course',
        'courses', 'teachers',
        ['teacher_id'], ['id'],
        ondelete='SET NULL'  # If a teacher is deleted, set the `teacher_id` to NULL
    )


def downgrade():
    """Remove the teacher_id foreign key from the courses table."""
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```