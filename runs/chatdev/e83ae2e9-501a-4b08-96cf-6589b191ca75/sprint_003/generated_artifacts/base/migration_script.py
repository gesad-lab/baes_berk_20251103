'''
Migration script to add email field to the Student entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Add the email column as nullable first
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Optionally, you can set a default value for existing records
    # op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # After ensuring all existing records have valid email values, alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')