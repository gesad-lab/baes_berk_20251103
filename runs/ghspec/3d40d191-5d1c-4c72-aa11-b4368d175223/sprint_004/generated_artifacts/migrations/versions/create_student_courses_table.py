from alembic import op
import sqlalchemy as sa

def upgrade():
    """Create the `student_courses` table to establish a many-to-many relationship between students and courses."""
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )

def downgrade():
    """Drop the `student_courses` table."""
    op.drop_table('student_courses')