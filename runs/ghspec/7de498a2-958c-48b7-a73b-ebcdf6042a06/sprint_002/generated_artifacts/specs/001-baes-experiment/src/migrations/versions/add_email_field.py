```python
"""Add email field to students table.

Revision ID: <revision_id>
Revises: <previous_revision_id>
Create Date: <timestamp>

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<revision_id>'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None

def upgrade():
    """Add the email column to the students table."""
    # This will add the 'email' column to the 'students' table
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    """Remove the email column from the students table."""
    # This will remove the 'email' column, reversing the change made in upgrade()
    op.drop_column('students', 'email')
```