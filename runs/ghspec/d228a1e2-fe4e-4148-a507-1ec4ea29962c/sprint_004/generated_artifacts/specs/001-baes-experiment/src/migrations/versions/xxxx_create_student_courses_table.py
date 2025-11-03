from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_create_student_courses_table'
down_revision = None  # Update with the previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Create the student_courses junction table."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='fk_student'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='fk_course'),
        sa.PrimaryKeyConstraint('student_id', 'course_id', name='pk_student_course')
    )

def downgrade():
    """Drop the student_courses junction table."""
    op.drop_table('student_courses')