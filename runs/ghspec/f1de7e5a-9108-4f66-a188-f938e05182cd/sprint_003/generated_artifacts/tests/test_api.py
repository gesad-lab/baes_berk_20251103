```python
# database_migrations.py

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection

# Revision identifiers, used by Alembic.
revision = 'add_courses_table'
down_revision = None  # Specify the previous revision here if any
branch_labels = None
depends_on = None

def upgrade():
    # Create the courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
    )

def downgrade():
    # Drop the courses table if it exists
    op.drop_table('courses')
```