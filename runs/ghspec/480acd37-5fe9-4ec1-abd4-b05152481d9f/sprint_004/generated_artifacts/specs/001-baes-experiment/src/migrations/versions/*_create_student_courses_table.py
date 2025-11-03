```python
"""Create student_courses table

Revision ID: <new_revision_id>
Revises: <previous_revision_id>
Create Date: <timestamp>
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '<new_revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None

def upgrade():
    """Create the student_courses junction table to represent the many-to-many relationship between students and courses."""
    op.create_table(
        'student_courses',
        sa.Column('id', sa.Integer(), primary_key=True),  # Unique identifier
        sa.Column('student_id', sa.Integer(), nullable=False),  # Foreign key for Student
        sa.Column('course_id', sa.Integer(), nullable=False),  # Foreign key for Course
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),  # Enforce relationship to Students
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE')  # Enforce relationship to Courses
    )

def downgrade():
    """Drop the student_courses table."""
    op.drop_table('student_courses')
```