```python
"""Database migrations for the application using Alembic."""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'  # Unique revision ID
down_revision = None  # Replace with previous revision ID if there is any
branch_labels = None
depends_on = None

def upgrade():
    """Create the Teacher table in the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),  # Primary key
        sa.Column('name', sa.String(), nullable=False),  # Teacher's name
        sa.Column('email', sa.String(), unique=True, nullable=False)  # Unique Teacher email
    )

def downgrade():
    """Drop the Teacher table in case of migration rollback."""
    op.drop_table('teachers')
```