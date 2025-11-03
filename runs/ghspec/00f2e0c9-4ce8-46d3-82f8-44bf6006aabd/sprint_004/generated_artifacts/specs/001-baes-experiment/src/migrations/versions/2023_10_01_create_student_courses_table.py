```python
"""Create student_courses table

Revision ID: 2023_10_01
Revises: 
Create Date: 2023-10-01 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_01'
down_revision = None  # Update this if there's a previous migration
branch_labels = None
depends_on = None


def upgrade():
    """Create student_courses junction table for many-to-many relationship
    between students and courses.
    """
    # Create the 'student_courses' table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )


def downgrade():
    """Drop the student_courses table."""
    op.drop_table('student_courses')
```