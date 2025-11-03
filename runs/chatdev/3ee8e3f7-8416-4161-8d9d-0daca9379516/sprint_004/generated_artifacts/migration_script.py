'''
Migration script to add Course table and email field to the students table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '20231001_001'  # Use a timestamp or a unique identifier
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column to the students table as nullable initially
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Update existing records with a default value (e.g., empty string)
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Alter the column to make it non-nullable after existing records are updated
    op.alter_column('students', 'email', nullable=False)
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Create the association table for student and course relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
def downgrade():
    # Remove the association table if needed
    op.drop_table('student_courses')
    # Remove the courses table if needed
    op.drop_table('courses')
    # Remove the email column if needed
    op.drop_column('students', 'email')