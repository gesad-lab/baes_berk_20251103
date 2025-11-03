```python
"""Add enrollments table for student-course relationship

Revision ID: <timestamp>
Revises: 
Create Date: <insert_date>
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Create the enrollments table to facilitate the many-to-many relationship."""
    op.create_table(
        'enrollments',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade():
    """Drop the enrollments table on downgrade."""
    op.drop_table('enrollments')
```