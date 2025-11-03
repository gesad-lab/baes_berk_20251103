"""Create teachers table

Revision ID: 2023_create_teacher_table
"""
from sqlalchemy import Column, Integer, String
from alembic import op


def upgrade():
    # Create the teachers table with the necessary fields
    op.create_table('teachers',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),  # Teacher's full name
        Column('email', String, nullable=False, unique=True)  # Teacher's unique email
    )


def downgrade():
    # Drop the teachers table if the migration is reversed
    op.drop_table('teachers')