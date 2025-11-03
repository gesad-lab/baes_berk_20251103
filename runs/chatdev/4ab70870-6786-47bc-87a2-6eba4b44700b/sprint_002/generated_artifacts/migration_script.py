'''
Database migration script for adding email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add the new email column with a default value
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, server_default='example@example.com'))
    # Update existing records to have a specific email format or value
    op.execute("UPDATE students SET email='example@example.com' WHERE email IS NULL")
def downgrade():
    op.drop_column('students', 'email')