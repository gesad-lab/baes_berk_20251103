```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230101_create_student_course_table'
down_revision = None  # Assumes there is no previous revision set
branch_labels = None
depends_on = None

def upgrade():
    """Create the Student_Course table for many-to-many relationship between students and courses."""
    op.create_table(
        'Student_Course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['Student.id']),
        sa.ForeignKeyConstraint(['course_id'], ['Course.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    """Drop the Student_Course table."""
    op.drop_table('Student_Course')
```