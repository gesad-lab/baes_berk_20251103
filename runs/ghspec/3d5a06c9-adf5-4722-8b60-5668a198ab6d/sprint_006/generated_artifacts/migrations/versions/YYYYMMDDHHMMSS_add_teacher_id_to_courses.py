```python
"""Add teacher_id to Courses

Revision ID: YYYYMMDDHHMMSS
Revises: previous_revision_id
Create Date: 2023-10-01 00:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'YYYYMMDDHHMMSS'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration to add the teacher_id column to the courses table."""
    # Adding the teacher_id column as a nullable integer
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    
    # Creating a foreign key constraint for teacher_id referencing the teachers table
    op.create_foreign_key(
        'fk_course_teacher',       # Constraint name
        'courses',                 # Source table
        'teachers',                # Target table
        ['teacher_id'],           # Source column
        ['id'],                   # Target column
        ondelete='SET NULL'       # Action on delete
    )


def downgrade():
    """Revert the migration by dropping the foreign key and column."""
    # Dropping the foreign key constraint
    op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
    
    # Dropping the teacher_id column
    op.drop_column('courses', 'teacher_id')
```