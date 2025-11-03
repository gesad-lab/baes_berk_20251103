from alembic import op
from sqlalchemy import Column, ForeignKey, Integer

def upgrade():
    # Create the student_courses junction table that establishes a many-to-many relationship
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), nullable=False),
        Column('course_id', Integer, ForeignKey('courses.id'), nullable=False),
        # Setting primary key as a composite of student_id and course_id
        primary_key=['student_id', 'course_id']
    )

def downgrade():
    # Drop the student_courses table if we need to roll back the migration
    op.drop_table('student_courses')