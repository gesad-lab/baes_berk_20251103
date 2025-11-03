```python
"""Create teachers table"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx' 
down_revision = 'previous_revision'

def upgrade():
    # Create the teachers table with the specified schema
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    # Drop the teachers table if we need to roll back
    op.drop_table('teachers')
```