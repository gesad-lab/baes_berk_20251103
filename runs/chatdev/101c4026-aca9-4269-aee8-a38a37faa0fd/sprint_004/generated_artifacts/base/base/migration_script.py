'''
Migration script to add email field to the Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with your revision ID
down_revision = None  # Replace with the previous revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Update existing records to have a default email value
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove the email column if needed
    op.drop_column('students', 'email')