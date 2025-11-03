```python
"""Add teacher_id to courses

Revision ID: <timestamp>
Revises: 
Create Date: 2023-10-04 12:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Add foreign key constraint linking teacher_id in courses to id in teachers
    op.create_foreign_key(
        'fk_courses_teachers',  # Constraint name
        'courses',              # Source table
        'teachers',             # Target table
        ['teacher_id'],         # Source column
        ['id'],                 # Target column
        ondelete='SET NULL'     # Action on delete of teacher
    )


def downgrade() -> None:
    # Remove foreign key constraint
    op.drop_constraint('fk_courses_teachers', 'courses', type_='foreignkey')

    # Drop the teacher_id column from courses table
    op.drop_column('courses', 'teacher_id')
```