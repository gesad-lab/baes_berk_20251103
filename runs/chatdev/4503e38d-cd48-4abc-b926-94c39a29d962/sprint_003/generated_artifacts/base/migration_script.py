'''
Migration script to add email field to Student entity.
'''
from sqlalchemy import Column, String
from alembic import op
def upgrade():
    # Make the email column nullable initially to preserve existing data
    op.add_column('students', Column('email', String, nullable=True))
def downgrade():
    op.drop_column('students', 'email')