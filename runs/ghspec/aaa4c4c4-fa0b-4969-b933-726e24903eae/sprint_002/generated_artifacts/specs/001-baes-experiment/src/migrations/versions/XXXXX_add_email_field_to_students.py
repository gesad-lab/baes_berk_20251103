```python
"""Add email field to students table

Revision ID: XXXXX
Revises: 
Create Date: YYYY-MM-DD HH:MM:SS.XXXXXX
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'XXXXX'
down_revision = None  # Update this based on your existing migration hierarchy
branch_labels = None
depends_on = None

def upgrade():
    """Add the email column to the students table."""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove the email column from the students table."""
    op.drop_column('students', 'email')
```