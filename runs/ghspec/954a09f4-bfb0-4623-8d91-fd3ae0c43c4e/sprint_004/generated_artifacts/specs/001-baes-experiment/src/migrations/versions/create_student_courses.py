"""Create student_courses table"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230901_create_student_courses'
down_revision = None  # Update this to the previous migration revision if applicable.

def upgrade():
    # Create the student_courses table that links students to courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    # Drop the student_courses table if the migration is reversed
    op.drop_table('student_courses')