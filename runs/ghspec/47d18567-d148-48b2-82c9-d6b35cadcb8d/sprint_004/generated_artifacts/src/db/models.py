```python
"""Create student_course join table

Revision ID: a1234567890
Revises: 
Create Date: 2023-10-01 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    # Create 'student_course' join table for many-to-many relationship
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )


def downgrade():
    # Drop 'student_course' join table
    op.drop_table('student_course')
```