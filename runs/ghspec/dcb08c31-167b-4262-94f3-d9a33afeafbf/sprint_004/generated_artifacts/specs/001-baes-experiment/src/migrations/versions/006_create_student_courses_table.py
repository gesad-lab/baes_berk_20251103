from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006_create_student_courses_table'
down_revision = '005_some_previous_migration'  # Update this with the actual previous migration ID
branch_labels = None
depends_on = None


def upgrade():
    """Create the student_courses join table."""
    # Create the student_courses association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )


def downgrade():
    """Drop the student_courses join table."""
    op.drop_table('student_courses')