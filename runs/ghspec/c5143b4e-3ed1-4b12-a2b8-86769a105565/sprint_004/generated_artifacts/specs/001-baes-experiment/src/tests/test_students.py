```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'yyyyyyyyyyyy'  # replace with your unique revision identifier
down_revision = None  # replace with the previous migration if applicable
branch_labels = None
depends_on = None


def upgrade():
    # Create the 'student_courses' junction table to establish many-to-many relation between students and courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
        sa.PrimaryKeyConstraint('student_id', 'course_id'),
        sa.UniqueConstraint('student_id', 'course_id')  # Ensure no duplicate entries
    )


def downgrade():
    # Drop the 'student_courses' table if we need to roll back the migration
    op.drop_table('student_courses')
```