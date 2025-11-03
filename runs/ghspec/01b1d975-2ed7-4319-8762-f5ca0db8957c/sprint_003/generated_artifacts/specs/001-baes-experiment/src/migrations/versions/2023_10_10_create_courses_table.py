```python
# migrations/versions/2023_10_10_create_courses_table.py

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2023_10_10_create_courses_table'
down_revision = None  # Change to the previous migration id if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Create the courses table in the database."""
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Ensure the size of 'level' aligns with predefined categorizations (optional: can add a check later)

def downgrade():
    """Drop the courses table from the database."""
    op.drop_table('courses')
```