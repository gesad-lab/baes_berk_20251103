'''
Handles database migrations for the Student and Course entities.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_relationship'
down_revision = 'add_email_to_student'
branch_labels = None
depends_on = None
def upgrade():
    '''Create courses table and add email column to students table.'''
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
    # Create the association table for students and courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )
    # Add email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Alter the email column to be non-nullable
    op.alter_column('students', 'email', existing_type=sa.String(), nullable=False)
def downgrade():
    '''Drop courses table and remove email column from students table.'''
    op.drop_table('student_courses')
    op.drop_table('courses')
    op.drop_column('students', 'email')