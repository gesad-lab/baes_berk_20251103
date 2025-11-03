'''
Migration script for adding email field to Student entity and creating Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
down_revision = 'add_email_field_to_student'  # Update this based on your last migration
def upgrade():
    # Check if the courses table already exists
    if not op.get_bind().has_table('courses'):
        # Create the courses table
        op.create_table(
            'courses',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False),
        )
    # Check if the student_courses association table already exists
    if not op.get_bind().has_table('student_courses'):
        # Create the association table for student and course relationship
        op.create_table(
            'student_courses',
            sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
            sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
        )
def downgrade():
    # Remove email column from the students table
    op.drop_column('students', 'email')
    # Drop the courses table
    op.drop_table('courses')
    # Drop the association table
    op.drop_table('student_courses')