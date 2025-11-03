```python
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = '2023_10_10_create_courses_table'
down_revision = None  # Adjust as necessary based on existing migrations
branch_labels = None
depends_on = None


def upgrade():
    # Create the courses table with required fields for name and level
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),  # Name is required
        sa.Column('level', sa.String, nullable=False),  # Level is required
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),  # Timestamp for record creation
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())  # Timestamp for updates
    )


def downgrade():
    # Drop the courses table if needed
    op.drop_table('courses')
```