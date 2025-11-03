```python
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'abcdefgh1234'  # Unique identifier for this migration
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Run database migrations to create the student_courses junction table."""
    op.create_table(
        'student_courses',
        sa.Column('id', sa.Integer(), nullable=False),  # Unique identifier for the record
        sa.Column('student_id', sa.Integer(), nullable=False),  # Foreign key to Student
        sa.Column('course_id', sa.Integer(), nullable=False),  # Foreign key to Course
        sa.PrimaryKeyConstraint('id'),  # Primary key constraint for the table
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE'),  # Cascading delete on student remove
        sa.ForeignKeyConstraint(['course_id'], ['course.id'], ondelete='CASCADE')  # Cascading delete on course removal
    )


def downgrade():
    """Revert the migration by dropping the student_courses table."""
    op.drop_table('student_courses')
```