```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Create the student_courses table to establish a many-to-many relationship 
    between students and courses."""
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    """Drop the student_courses table to reverse the upgrade operation."""
    op.drop_table('student_courses')
```