```python
"""create_course_table.py

Migration file to create the Course table in the database
with fields for name and level.
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxx_create_course_table'  # Replace with actual revision ID
down_revision = None  # Set to previous revision ID if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Create the Course table with required fields."""
    # Creating the 'course' table with 'name' and 'level' as required string fields
    op.create_table(
        'course',
        sa.Column('id', sa.Integer, primary_key=True),  # Adding an ID column for primary key
        sa.Column('name', sa.String(length=100), nullable=False),  # Name field, required
        sa.Column('level', sa.String(length=50), nullable=False)  # Level field, required
    )

def downgrade():
    """Drop the Course table during a migration rollback."""
    op.drop_table('course')
```