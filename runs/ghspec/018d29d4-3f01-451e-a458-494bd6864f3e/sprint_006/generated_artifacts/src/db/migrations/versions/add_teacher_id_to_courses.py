```python
"""Add teacher_id column to courses table

Revision ID: <unique_revision_id>
Revises: <previous_revision_id>
Create Date: <current_date>
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<unique_revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add teacher_id to courses"""
    # Adding `teacher_id` column to `courses` table with a foreign key reference to the `teachers` table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))


def downgrade():
    """Revert the migration by removing teacher_id from courses"""
    # Dropping the `teacher_id` column from the `courses` table
    op.drop_column('courses', 'teacher_id')
```