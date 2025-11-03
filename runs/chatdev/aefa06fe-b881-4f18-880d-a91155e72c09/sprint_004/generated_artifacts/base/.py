'''
Migration script to add email column to the existing students table.
'''
from sqlalchemy import Column, String
from alembic import op
def upgrade():
    op.add_column('students', Column('email', String, nullable=False))
def downgrade():
    op.drop_column('students', 'email')