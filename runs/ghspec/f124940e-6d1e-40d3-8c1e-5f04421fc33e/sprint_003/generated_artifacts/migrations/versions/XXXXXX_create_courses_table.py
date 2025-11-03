```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'XXXXXX'  # Replace with an actual revision ID
down_revision = None  # Replace with the previous migration ID if available
branch_labels = None
depends_on = None

def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('level', sa.String, nullable=False),
    )

def downgrade():
    # Drop the courses table if we need to rollback the migration
    op.drop_table('courses')
```