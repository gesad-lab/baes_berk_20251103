```python
"""Add email column to Student table.

Revision ID: XXXX
Revises: YYYY
Create Date: 2023-10-16 12:00:00
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'XXXX'
down_revision = 'YYYY'
branch_labels = None
depends_on = None

def upgrade():
    """Add email column to student table."""
    # Adding the email column with a nullable constraint
    op.add_column('student', sa.Column('email', sa.String(length=255), nullable=True))

def downgrade():
    """Remove email column from student table."""
    # Dropping the email column to revert changes
    op.drop_column('student', 'email')
```