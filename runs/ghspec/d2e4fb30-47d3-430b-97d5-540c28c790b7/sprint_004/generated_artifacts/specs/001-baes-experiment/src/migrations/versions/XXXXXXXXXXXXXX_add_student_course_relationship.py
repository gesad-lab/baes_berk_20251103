```python
"""Add Student-Course Relationship

Create a linking table to establish a many-to-many relationship 
between students and courses.
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'XXXXXXXXXXXXXX'  # Replace with a unique revision ID
down_revision = None  # Replace with the ID of the previous migration
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create the student_courses table for many-to-many relationships."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade() -> None:
    """Drop the student_courses table to revert migration changes."""
    op.drop_table('student_courses')
```