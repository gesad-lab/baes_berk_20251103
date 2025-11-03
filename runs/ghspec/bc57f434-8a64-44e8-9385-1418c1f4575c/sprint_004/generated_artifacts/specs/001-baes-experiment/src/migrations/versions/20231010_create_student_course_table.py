```python
"""Create StudentCourse table

Revision ID: 20231010_create_student_course_table
Revises: 
Create Date: 2023-10-10 00:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20231010_create_student_course_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply migrations to create the StudentCourse table."""
    # Create the StudentCourse table to manage the many-to-many relationship
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE'),  # Assuming 'student.id' is the primary key
        sa.ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE'),  # Assuming 'course.id' is the primary key
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade() -> None:
    """Remove the StudentCourse table."""
    op.drop_table('student_course')
```