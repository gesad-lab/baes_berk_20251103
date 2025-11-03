'''
Database migration script for adding email field to Student entity and creating Course table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add the new email column
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))
    # Update existing records to have a specific email format or unique value
    op.execute("UPDATE students SET email='student_' || id || '@example.com' WHERE email IS NULL")
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )
def downgrade():
    op.drop_table('courses')
    op.drop_column('students', 'email')