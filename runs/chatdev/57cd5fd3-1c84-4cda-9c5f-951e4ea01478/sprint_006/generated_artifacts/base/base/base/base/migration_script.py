'''
Alembic migration script to add email field to Student table.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Populate existing records with a default value (if applicable)
    # You can set a default value or leave it as NULL
    # Example: op.execute("UPDATE students SET email = 'default@example.com' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')