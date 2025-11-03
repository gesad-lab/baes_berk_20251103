```python
# /src/database/migrations/001_add_teachers_table.py

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '001_add_teachers_table'
down_revision = None  # Set this to the revision of the previous migration
branch_labels = None
depends_on = None

def upgrade():
    """Create the teachers table in the database."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),  # Auto-incrementing ID
        sa.Column('name', sa.String(), nullable=False),  # Teacher's name (required)
        sa.Column('email', sa.String(), nullable=False, unique=True)  # Unique email (required)
    )

def downgrade():
    """Drop the teachers table from the database."""
    op.drop_table('teachers')  # Remove the teachers table if it exists
```