```python
"""Create teachers table

Revision ID: abc123
Revises: previous_revision_id
Create Date: 2023-10-30 12:00:00
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError

# revision identifiers, used by Alembic.
revision = 'abc123'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    # Create the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),  # Auto-generated ID for each teacher
        sa.Column('name', sa.String(length=255), nullable=False),  # Teacher's name, required
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)  # Teacher's email, required and unique
    )

def downgrade():
    # Drop the teachers table if it needs to be reverted
    op.drop_table('teachers')
```