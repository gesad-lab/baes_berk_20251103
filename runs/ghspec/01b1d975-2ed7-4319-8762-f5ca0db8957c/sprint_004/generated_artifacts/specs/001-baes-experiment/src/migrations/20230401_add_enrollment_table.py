from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230401_add_enrollment_table'
down_revision = None  # Update this to the last migration ID as needed
branch_labels = None
depends_on = None

def upgrade():
    """Create the enrollments association table linking students and courses."""
    op.create_table(
        'enrollments',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    """Drop the enrollments table."""
    op.drop_table('enrollments')