'''
Handles database migrations for the Student and Course entities.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'add_course_table'
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
    # Add email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Here you can add logic to populate the email column if needed
    # For example, you could set a default value or handle existing records
    # Alter the email column to be non-nullable
    op.alter_column('students', 'email', existing_type=sa.String(), nullable=False)
def downgrade():
    '''Drop courses table and remove email column from students table.'''
    op.drop_table('courses')
    op.drop_column('students', 'email')