```python
"""Add student_course relationship table

Revision ID: 123456789abc
Revises: 
Create Date: 2023-10-03 12:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None  # Adjust if there's a previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Creates the student_course junction table to establish a many-to-many relationship."""
    # Create the junction table with foreign keys to Student and Course tables
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id'),  # Composite primary key
        # Optionally add timestamps
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

def downgrade():
    """Drops the student_course junction table."""
    op.drop_table('student_course')
```