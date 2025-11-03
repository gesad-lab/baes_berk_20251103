```python
"""Create student_courses association table

Revision ID: XXXXXXXXXXXX
Revises: 
Create Date: 2023-10-04 00:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'XXXXXXXXXXXX'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create a new table to associate students with courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('student.id'), nullable=False),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('course.id'), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    # Ensure that existing relationships can be established by combining both entities
    # Additional constraints or changes can be added if required in the future


def downgrade():
    # Drop the student_courses table if it exists during a downgrade
    op.drop_table('student_courses')
```