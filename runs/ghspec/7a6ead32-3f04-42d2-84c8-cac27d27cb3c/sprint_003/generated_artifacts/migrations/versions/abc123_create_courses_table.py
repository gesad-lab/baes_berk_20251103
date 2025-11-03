"""Create courses table

Revision ID: abc123
Revises: previous_revision_id
Create Date: 2023-10-10 13:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'abc123'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    # Create 'courses' table with required fields
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),  # Course name
        sa.Column('level', sa.String(), nullable=False)  # Course level
    )

def downgrade():
    # Drop 'courses' table on migration rollback
    op.drop_table('courses')