```python
from sqlalchemy import create_engine, Column, Integer, String
from alembic import op

def downgrade() -> None:
    """Remove the courses table from the database."""
    # Drop the courses table if it exists
    op.drop_table('courses')
```