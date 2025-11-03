```python
import sqlalchemy as sa
from alembic import op
import logging

# Get the logger
logger = logging.getLogger("alembic.migration")

# Revision identifiers, used by Alembic.
revision = 'add_teacher_table'
down_revision = None  # Update with the correct revision if this is not the first migration
branch_labels = None
depends_on = None

def upgrade():
    """Creates the Teachers table."""
    # Create the teachers table with id, name and email
    logger.info("Creating teachers table.")
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),  # Primary Key
        sa.Column('name', sa.String(), nullable=False),  # Required field
        sa.Column('email', sa.String(), nullable=False, unique=True)  # Required and unique field
    )
    logger.info("Teachers table created successfully.")


def downgrade():
    """Drops the Teachers table."""
    logger.info("Dropping teachers table.")
    op.drop_table('teachers')
    logger.info("Teachers table dropped successfully.")
```