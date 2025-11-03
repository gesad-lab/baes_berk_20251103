'''
Database migration script to add Course table and email field to the Student table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Update existing records to set a default value (e.g., empty string)
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 3: Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
    # Step 4: Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('courses')
    op.drop_column('students', 'email')