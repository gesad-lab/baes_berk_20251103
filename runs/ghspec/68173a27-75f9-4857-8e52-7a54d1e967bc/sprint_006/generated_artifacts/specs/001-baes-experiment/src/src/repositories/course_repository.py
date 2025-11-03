```python
"""Add teacher_id column to courses table

Revision ID: <revision_id>
Revises: <previous_revision_id>
Create Date: <create_date>
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade the database schema to add teacher_id to courses."""
    # Adding the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    # Creating a foreign key constraint linking teacher_id to the teachers table
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade() -> None:
    """Downgrade the database schema by removing teacher_id from courses."""
    # Dropping the foreign key constraint for teacher_id
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    # Dropping the teacher_id column from the courses table
    op.drop_column('courses', 'teacher_id')
```