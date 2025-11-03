```python
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = '001_create_student_courses'
down_revision = None  # Update if there is a previous migration
branch_labels = None
depends_on = None


def upgrade():
    """Create the student_courses table to establish a many-to-many relationship between Students and Courses."""
    # Creating the student_courses table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')  # Composite primary key
    )


def downgrade():
    """Drop the student_courses table."""
    op.drop_table('student_courses')
```