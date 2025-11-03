'''
Migration script to add email column to the students table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))  
    # Update existing records to have a default email or handle them as needed
    op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # After ensuring existing data is handled, you can alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')  # Remove email column