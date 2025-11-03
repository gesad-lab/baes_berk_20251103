'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = 'xxxxxx'  # Replace with a unique revision ID
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    # Add the email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, you can set a default value for existing records
    # op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Then alter the column to be non-nullable if needed
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')