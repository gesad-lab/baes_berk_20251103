```python
# src/database.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'abc123'  # Update with an appropriate revision ID
down_revision = None  # Depending on your setup, set the previous revision ID
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration to create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )

def downgrade():
    """Revert the migration by dropping the teachers table."""
    op.drop_table('teachers')
```