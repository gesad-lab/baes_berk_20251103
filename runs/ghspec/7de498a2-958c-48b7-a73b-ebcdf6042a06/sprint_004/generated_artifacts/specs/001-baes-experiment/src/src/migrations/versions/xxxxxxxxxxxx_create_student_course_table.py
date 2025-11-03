from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxxxxxxxxxx'  # Replace with actual revision ID
down_revision = None  # Update depending on the previous migration
branch_labels = None
depends_on = None


def upgrade():
    """Create the student_courses association table."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
    )


def downgrade():
    """Drop the student_courses association table."""
    op.drop_table('student_courses')