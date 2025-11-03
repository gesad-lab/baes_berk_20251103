"""Create teacher table

Revision ID: 2023xxxx
Revises: yyyyyyyy
Create Date: 2023-10-03 12:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Creating the 'teachers' table with 'id', 'name' and 'email' as columns
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),  # 'name' is required
        sa.Column('email', sa.String, unique=True, nullable=False)  # 'email' is required and must be unique
    )

def downgrade():
    # Dropping the 'teachers' table in case we need to revert the migration
    op.drop_table('teachers')