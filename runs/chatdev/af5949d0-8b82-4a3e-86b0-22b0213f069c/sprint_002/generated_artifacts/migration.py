'''
Migration script to add email field to the Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Update existing records to set a default value for email
    connection = op.get_bind()
    connection.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 3: Alter the email column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove the email column from the students table
    op.drop_column('students', 'email')