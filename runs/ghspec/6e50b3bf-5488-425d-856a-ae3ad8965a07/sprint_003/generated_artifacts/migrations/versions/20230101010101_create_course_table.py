```python
from flask_sqlalchemy import SQLAlchemy
from alembic import op
import sqlalchemy as sa

# Define the database object
db = SQLAlchemy()

# Revision identifiers, used by Alembic.
revision = '20230101010101'
down_revision = None
Branch_label = None
depends_on = None

def upgrade():
    """Create the 'courses' table."""
    # Create the courses table with the specified columns
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('level', sa.String(length=50), nullable=False)
    )

def downgrade():
    """Drop the 'courses' table."""
    # Drop the courses table if it exists
    op.drop_table('courses')
```