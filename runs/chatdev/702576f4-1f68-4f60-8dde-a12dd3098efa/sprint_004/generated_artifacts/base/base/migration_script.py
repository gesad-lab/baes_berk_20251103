'''
Migration script to add email field to Student entity.
'''
from alembic import op
import sqlalchemy as sa
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    # Step 2: Update existing records with a default email value (e.g., 'noemail@example.com')
    op.execute("UPDATE students SET email = 'noemail@example.com' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')