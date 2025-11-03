from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_student_course_association'
down_revision = None  # Update this if you have a base migration
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the student_course association table."""
    # Create a new table to associate students with courses
    op.create_table('student_course',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    """Revert the migration by dropping the student_course association table."""
    op.drop_table('student_course')