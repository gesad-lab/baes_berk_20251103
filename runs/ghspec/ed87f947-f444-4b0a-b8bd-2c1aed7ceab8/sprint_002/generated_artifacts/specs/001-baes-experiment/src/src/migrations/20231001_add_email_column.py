"""Add email column to the students table

Revision ID: 20231001
"""
from sqlalchemy import Column, String
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection


def upgrade():
    # Add the email column to the students table with a non-null constraint
    op.add_column('students', Column('email', String, nullable=False))

    # Detailed verification and migration handling if necessary
    bind = op.get_bind()
    inspector = reflection.Inspector.from_engine(bind)
    
    # Check if the column already exists to prevent errors during multiple run scenarios
    if 'email' not in [col['name'] for col in inspector.get_columns('students')]:
        op.add_column('students', Column('email', String, nullable=False))
    

def downgrade():
    # Remove the email column from the students table to rollback the migration
    op.drop_column('students', 'email')
"""