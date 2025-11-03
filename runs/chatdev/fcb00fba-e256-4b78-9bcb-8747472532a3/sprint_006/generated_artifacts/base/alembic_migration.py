'''
Migration script to add Teacher table, and preserve existing Student and Course data.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with the generated revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column to the students table with nullable=True
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Update existing records to set a default value for email
    op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
    # Create the association table
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
    )
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
    )
def downgrade():
    # Remove the teachers table if needed
    op.drop_table('teachers')
    # Remove the email column if needed
    op.drop_column('students', 'email')
    # Drop the courses table if needed
    op.drop_table('courses')
    # Drop the association table if needed
    op.drop_table('student_courses')