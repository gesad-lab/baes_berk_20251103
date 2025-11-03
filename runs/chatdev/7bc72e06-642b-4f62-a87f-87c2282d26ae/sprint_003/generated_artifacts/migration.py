'''
Migration script for adding email field to Student entity and creating Course table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
down_revision = 'add_email_field_to_student'  # Update this based on your last migration
def upgrade():
    # Add email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, unique=True))
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    # Remove email column from the students table
    op.drop_column('students', 'email')
    # Drop the courses table
    op.drop_table('courses')