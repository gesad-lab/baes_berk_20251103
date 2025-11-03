```python
"""Create teachers table

Revision ID: 890efb731b82
Revises: previous_revision_id
Create Date: 2023-10-01 12:00:00

"""
from alembic import op
import sqlalchemy as sa

revision = '890efb731b82'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    # Create the 'teachers' table with 'id', 'name', and 'email' fields
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), unique=True, nullable=False),
    )

def downgrade():
    # Drop the 'teachers' table if it exists
    op.drop_table('teachers')
```