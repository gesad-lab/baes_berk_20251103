'''
Migration script to add email field to the students table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column to the students table as nullable initially
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, update existing records with a default value (e.g., empty string)
    op.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Alter the column to make it non-nullable after existing records are updated
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove the email column if needed
    op.drop_column('students', 'email')