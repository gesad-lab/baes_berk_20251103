'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with actual revision ID
down_revision = 'yyyyyy'  # Replace with actual down revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add email column to students table as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, update existing records to set a default value for email
    # This step is only necessary if you want to ensure that existing records have a valid email
    # op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove email column from students table
    op.drop_column('students', 'email')