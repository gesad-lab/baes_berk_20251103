from alembic import op
from sqlalchemy import Column, Integer, ForeignKey

# Migration script for creating the StudentCourses junction table

def upgrade():
    """Create the student_courses table and establish the relationship
    between students and courses."""
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )


def downgrade():
    """Drop the student_courses table to reverse the migration."""
    op.drop_table('student_courses')