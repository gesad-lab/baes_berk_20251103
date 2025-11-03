"""create_teachers_table

Revision ID: xxx_revisions
Revises: previous_revision_id
Create Date: YYYY-MM-DD
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    # Drop the teacher table if it exists
    op.drop_table('teachers')