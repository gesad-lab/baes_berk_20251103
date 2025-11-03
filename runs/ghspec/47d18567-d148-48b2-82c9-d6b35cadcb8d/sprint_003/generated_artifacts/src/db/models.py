"""Create courses table

Revision ID: xxxxxxxx
Revises: 
Create Date: 2023-xx-xx xx:xx:xx.xxxxxx
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    # Create the courses table with the specified fields
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),  # Name field cannot be null
        sa.Column('level', sa.String, nullable=False)  # Level field cannot be null
    )


def downgrade():
    # Drop the courses table if it needs to be reverted
    op.drop_table('courses')