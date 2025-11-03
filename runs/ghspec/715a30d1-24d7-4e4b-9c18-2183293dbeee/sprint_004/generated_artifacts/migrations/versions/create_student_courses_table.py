from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'create_student_courses_table'
down_revision = None  # Specify the previous migration if there is one
branch_labels = None
depends_on = None


def upgrade():
    """Create the student_courses table."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )


def downgrade():
    """Drop the student_courses table."""
    op.drop_table('student_courses')