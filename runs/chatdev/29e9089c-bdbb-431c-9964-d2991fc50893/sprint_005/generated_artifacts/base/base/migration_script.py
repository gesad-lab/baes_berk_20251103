'''
Alembic migration script to add email column to students table and create courses table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Update existing records to have a default email value
    op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable after ensuring all records have valid email
    op.alter_column('students', 'email', existing_type=sa.String(), nullable=False)
    # Step 4: Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )
def downgrade():
    op.drop_table('courses')
    op.drop_column('students', 'email')