```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxx'  # Replace with the actual revision id
down_revision = 'yyyyyyy'  # Replace with the last revision id
branch_labels = None
depends_on = None

def upgrade():
    """Execute the upgrade to create the 'courses' table."""
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    """Execute the downgrade to remove the 'courses' table."""
    # Drop courses table
    op.drop_table('courses')
```