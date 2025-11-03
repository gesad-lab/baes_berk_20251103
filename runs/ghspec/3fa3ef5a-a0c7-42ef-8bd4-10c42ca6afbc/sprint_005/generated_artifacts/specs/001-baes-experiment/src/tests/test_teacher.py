```python
# migrations/versions/2023_10_01_0001_add_teachers_table.py
"""Add teachers table

Revision ID: 2023_10_01_0001
Revises: 
Create Date: 2023-10-01 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_01_0001'
down_revision = None  # Adjust according to your current migrations
branch_labels = None
depends_on = None

def upgrade():
    """Create teachers table"""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),  # Primary key
        sa.Column('name', sa.String(length=255), nullable=False),  # Teacher name, must be provided
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)  # Teacher email, must be unique and provided
    )

def downgrade():
    """Drop teachers table"""
    op.drop_table('teachers')
```