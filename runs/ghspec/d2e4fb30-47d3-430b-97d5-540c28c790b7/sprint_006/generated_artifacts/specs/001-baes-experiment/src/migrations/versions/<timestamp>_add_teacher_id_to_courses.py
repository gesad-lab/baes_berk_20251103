```python
"""add_teacher_id_to_courses

Revision ID: <timestamp>
Revises: <previous_revision_id>
Create Date: <date>

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add teacher_id column to courses table and set up foreign key constraint."""
    # Add new column 'teacher_id' to the existing 'courses' table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    # Create a foreign key constraint linking 'teacher_id' to 'id' field in 'teachers' table
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])


def downgrade() -> None:
    """Remove teacher_id column from courses table and drop foreign key constraint."""
    # Drop the foreign key constraint before removing the column
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    # Remove the 'teacher_id' column from the 'courses' table
    op.drop_column('courses', 'teacher_id')
```