```python
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<timestamp>'
down_revision = None  # Set this to the previous revision ID if not the first migration
branch_labels = None
depends_on = None


def upgrade():
    """Add the teachers table to the database."""
    # Creating the teachers table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True)
    )


def downgrade():
    """Drop the teachers table from the database."""
    op.drop_table('teachers')
```