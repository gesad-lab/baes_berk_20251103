# migrations/versions/xxxx_create_teachers_table.py

"""Create teachers table

Revision ID: xxxx
Revises: (previous revision)
Create Date: (create date)
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'  # Replace with actual revision ID
down_revision = None  # Replace with actual previous revision ID
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Apply the upgrade by creating the teachers table in the database."""
    op.create_table(
        'teachers',  # Name of the new table
        sa.Column('id', sa.Integer(), primary_key=True),  # Teacher ID (Primary Key)
        sa.Column('name', sa.String(), nullable=False),  # Teacher's name (Required)
        sa.Column('email', sa.String(), nullable=False)  # Teacher's email (Required)
    )

def downgrade() -> None:
    """Revert the upgrade by dropping the teachers table."""
    op.drop_table('teachers')  # Drop the teachers table on downgrade