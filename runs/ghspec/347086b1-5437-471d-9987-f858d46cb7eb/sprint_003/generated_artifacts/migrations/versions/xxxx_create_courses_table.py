"""Create courses table

Revision ID: xxxx
Revises: (no previous revision)
Create Date: (create date)
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create the courses table with required fields: name and level
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True),  # Primary key
        sa.Column('name', sa.String(), nullable=False),    # Course name, cannot be null
        sa.Column('level', sa.String(), nullable=False),   # Course level, cannot be null
    )

def downgrade() -> None:
    # Drop the courses table during a downgrade
    op.drop_table('courses')