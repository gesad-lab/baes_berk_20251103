from alembic import op
from sqlalchemy import Column, Integer, String

def downgrade():
    """Drops the teachers table from the database."""
    # Use op.drop_table to remove the 'teachers' table if it exists
    op.drop_table('teachers')