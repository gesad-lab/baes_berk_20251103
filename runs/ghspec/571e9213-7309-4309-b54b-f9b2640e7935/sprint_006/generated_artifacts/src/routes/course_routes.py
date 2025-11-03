```python
# src/routes/course_routes.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from alembic import op
import sqlalchemy as sa

# Assuming previous defined models have been imported
from models.course import Course
from models.teacher import Teacher

# Alembic Migration Script for adding teacher_id to courses table
def upgrade():
    """Add teacher_id to courses table."""
    # Add the teacher_id column to the courses table
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))

    # Create ForeignKey relationship with the teachers table
    op.create_foreign_key(
        'fk_courses_teacher',
        'courses', 'teachers',
        ['teacher_id'], ['id'],
        ondelete='SET NULL'  # Change this as per app requirements (e.g., CASCADE, SET NULL)
    )


def downgrade():
    """Remove teacher_id from courses table."""
    # Drop the ForeignKey constraint
    op.drop_constraint('fk_courses_teacher', 'courses', type_='foreignkey')
    
    # Remove the teacher_id column
    op.drop_column('courses', 'teacher_id')
```