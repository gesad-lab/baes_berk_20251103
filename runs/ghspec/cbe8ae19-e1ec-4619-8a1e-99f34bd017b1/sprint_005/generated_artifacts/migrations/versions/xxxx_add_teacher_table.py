```python
"""Migration script to add the Teacher table."""

from sqlalchemy import Column, Integer, String
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxx_add_teacher_table'
down_revision = None  # Change this to the previous migration id if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True)
    )
    
    # Ensure that the name is non-empty and the email is valid
    # Note: Actual validation logic should be handled in the service layer where the data is processed.

def downgrade():
    """Revert the migration by dropping the teachers table."""
    op.drop_table('teachers')
```