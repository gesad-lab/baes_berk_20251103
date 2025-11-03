```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the 'teachers' table with the required columns
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False)
    )

def downgrade():
    # Drop the 'teachers' table if the migration is rolled back
    op.drop_table('teachers')
```