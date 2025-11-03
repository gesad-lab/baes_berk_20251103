```python
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'add_teachers_table'
down_revision = None  # Specify the previous revision ID if applicable
branch_labels = None
depends_on = None


def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True)
    )


def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')
```