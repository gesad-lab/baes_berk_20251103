```python
"""empty message"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx_add_student_courses_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Creates the student_courses association table."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id'),
        sa.UniqueConstraint('student_id', 'course_id', name='uq_student_course')
    )


def downgrade():
    """Drops the student_courses association table."""
    op.drop_table('student_courses')
```