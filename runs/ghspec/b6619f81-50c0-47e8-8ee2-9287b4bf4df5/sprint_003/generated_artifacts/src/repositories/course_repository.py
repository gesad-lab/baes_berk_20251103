```python
# migrations/create_courses_table.py

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1234567890ab'  # Unique revision identifier
down_revision = None        # Previous revision identifier
branch_labels = None       # Optional; use for branch label
depends_on = None          # Optional; use for dependencies

def upgrade() -> None:
    """Upgrade the database schema to include the courses table."""
    # Create the courses table with required fields
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),  # name is a required field
        sa.Column('level', sa.String, nullable=False)  # level is a required field
    )

def downgrade() -> None:
    """Revert the database schema to remove the courses table."""
    # Drop the courses table if it exists
    op.drop_table('courses')
```