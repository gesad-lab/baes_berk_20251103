```python
"""create_student_courses_table

Revision ID: xyz987
Revises: 
Create Date: 2023-10-10 10:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xyz987'
down_revision = None  # Replace with the last revision ID if you have one
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply the migration to create the student_courses junction table."""
    # Create the student_courses junction table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade() -> None:
    """Revert the migration by dropping the student_courses table."""
    # Drop the student_courses junction table
    op.drop_table('student_courses')
```