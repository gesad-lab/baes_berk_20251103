'''
Migration script to add Course table, email field to the Student table, and create Teacher table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your revision ID
down_revision = None  # Replace with your previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True)  # Added teacher_id
    )
    # Add email column to students table, make it nullable to preserve existing data
    op.add_column('students', sa.Column('email', sa.String, nullable=True))
    # Create the association table for students and courses
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Drop association table
    op.drop_table('student_courses')
    # Drop courses table
    op.drop_table('courses')
    # Drop email column from students table
    op.drop_column('students', 'email')
    # Drop teachers table
    op.drop_table('teachers')