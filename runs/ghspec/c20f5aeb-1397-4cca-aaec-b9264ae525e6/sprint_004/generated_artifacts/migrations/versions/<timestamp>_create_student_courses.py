```python
"""create_student_courses.py

Migration script to create the 'student_courses' table that establishes a
many-to-many relationship between students and courses. The table will
preserve existing records and facilitate new enrollments.
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Apply the migration to create the student_courses table."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade():
    """Revert the migration by dropping the student_courses table."""
    op.drop_table('student_courses')
```