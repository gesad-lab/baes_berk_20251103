```python
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Update with the previous migration ID, if applicable
branch_labels = None
depends_on = None


def upgrade():
    """Create the Teacher table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )


def downgrade():
    """Drop the Teacher table."""
    op.drop_table('teachers')
```