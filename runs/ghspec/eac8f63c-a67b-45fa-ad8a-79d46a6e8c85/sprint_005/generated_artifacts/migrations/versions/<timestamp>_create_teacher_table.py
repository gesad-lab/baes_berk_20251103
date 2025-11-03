```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Create the teachers table to store teacher information."""
    op.create_table('teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )

def downgrade():
    """Drop the teachers table during a migration rollback."""
    op.drop_table('teachers')
```