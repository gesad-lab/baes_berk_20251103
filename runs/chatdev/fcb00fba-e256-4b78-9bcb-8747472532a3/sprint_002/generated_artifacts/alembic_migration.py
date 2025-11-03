'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with the generated revision ID
down_revision = None  # Replace with the previous revision ID if applicable
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column to the students table with nullable=True
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, you can set a default value for existing records
    # op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # After ensuring existing data is handled, alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    # Remove the email column if needed
    op.drop_column('students', 'email')