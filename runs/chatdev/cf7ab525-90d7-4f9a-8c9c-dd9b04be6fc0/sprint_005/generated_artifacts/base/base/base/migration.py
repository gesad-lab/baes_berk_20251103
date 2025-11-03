'''
Migration script to add email column to the students table.
'''
from sqlalchemy import Column, String
from alembic import op
def upgrade():
    # Add the email column as required
    op.add_column('students', Column('email', String, nullable=False))
    # Optionally, you may want to set a default value or update existing records to avoid issues
def downgrade():
    op.drop_column('students', 'email')