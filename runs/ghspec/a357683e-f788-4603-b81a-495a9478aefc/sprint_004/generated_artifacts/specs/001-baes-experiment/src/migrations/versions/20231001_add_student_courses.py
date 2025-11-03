```python
from sqlalchemy import Column, Integer, ForeignKey
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20231001_add_student_courses'
down_revision = None  # Update this value to the last migration revision if there are previous migrations.
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Create the student_courses table to link students with courses."""
    # Create the student_courses table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade() -> None:
    """Drop the student_courses table if it exists."""
    # Drop the student_courses table
    op.drop_table('student_courses')
```