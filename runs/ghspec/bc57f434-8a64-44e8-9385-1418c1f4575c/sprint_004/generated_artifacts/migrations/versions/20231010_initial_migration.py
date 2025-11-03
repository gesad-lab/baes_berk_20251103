```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20231010_initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    """Create the student_course table to manage many-to-many relationships between students and courses."""
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    """Drop the student_course table."""
    op.drop_table('student_course')
```