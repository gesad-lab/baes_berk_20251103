'''
Migration script to add email field to the Student table.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with the actual revision ID
down_revision = 'yyyyyy'  # Replace with the actual down revision ID
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, you can set a default value for existing records if needed
    # op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Then alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')