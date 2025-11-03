```python
"""Add email field to Student table

Revision ID: [timestamp]
Revises: 
Create Date: [timestamp]

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '[timestamp]'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    """Add email column to the students table"""
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove email column from the students table"""
    op.drop_column('students', 'email')
```