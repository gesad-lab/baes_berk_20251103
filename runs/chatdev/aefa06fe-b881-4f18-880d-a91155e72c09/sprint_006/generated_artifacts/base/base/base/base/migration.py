'''
Migration script to add email column to the existing students table.
'''
from sqlalchemy import Column, String
from alembic import op
def upgrade():
    # Step 1: Add the email column as nullable
    op.add_column('students', Column('email', String, nullable=True))
    # Step 2: Populate existing records with a default value
    connection = op.get_bind()
    connection.execute("UPDATE students SET email = '' WHERE email IS NULL")
    # Step 3: Alter the column to be non-nullable
    op.alter_column('students', 'email', nullable=False)
def downgrade():
    op.drop_column('students', 'email')