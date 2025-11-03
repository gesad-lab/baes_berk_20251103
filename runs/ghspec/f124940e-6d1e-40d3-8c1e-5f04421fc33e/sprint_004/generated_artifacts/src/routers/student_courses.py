```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxxxxxxx'
down_revision = 'xxxxxxxxxxxx'
branch_labels = None
depends_on = None

def upgrade():
    # Create student_courses table to establish many-to-many relationship between students and courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )

def downgrade():
    # Drop student_courses table if the migration is rolled back
    op.drop_table('student_courses')
```