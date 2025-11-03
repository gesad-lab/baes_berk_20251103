from alembic import op
from sqlalchemy import Column, Integer, ForeignKey

# Upgrade function to create the student_courses table
def upgrade():
    # Create the student_courses table with foreign key relationships to students and courses
    op.create_table(
        'student_courses',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('student_id', Integer, ForeignKey('students.id'), nullable=False),
        Column('course_id', Integer, ForeignKey('courses.id'), nullable=False)
    )

# Downgrade function to drop the student_courses table
def downgrade():
    # Drop the student_courses table if it exists
    op.drop_table('student_courses')