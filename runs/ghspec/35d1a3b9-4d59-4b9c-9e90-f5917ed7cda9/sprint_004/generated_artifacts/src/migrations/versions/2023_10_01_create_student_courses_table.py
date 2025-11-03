from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '2023_10_01_create_student_courses_table'
down_revision = None  # Update this if there's a previous migration
branch_labels = None
depends_on = None

def upgrade():
    # Create a new table `student_courses` for many-to-many relationship between Students and Courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    # Drop the `student_courses` table if we need to rollback the migration
    op.drop_table('student_courses')