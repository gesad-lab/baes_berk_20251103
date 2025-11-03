'''
Migration script to add email column to the Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column to the students table
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))  # Allow NULL temporarily
    # Update existing records to set a default value for the new email column
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")  # Set default value
    # Alter the column to make it required
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove the email column if needed
    op.drop_column('students', 'email')