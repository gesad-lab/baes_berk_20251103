```python
import sqlalchemy as sa
from alembic import op
import logging

# Initialize logging
logger = logging.getLogger(__name__)

# Revision identifiers, used by Alembic.
revision = '001_add_email_to_students'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Apply the migration by adding an email column to the students table."""
    try:
        # Add a new column 'email' to the 'students' table
        op.add_column('students', sa.Column('email', sa.String(length=255), nullable=True))
        logger.info("Added 'email' column to 'students' table successfully.")

    except Exception as e:
        logger.error("Error adding 'email' column to 'students' table: %s", e)
        raise


def downgrade():
    """Revert the migration by removing the added email column."""
    try:
        # Remove the 'email' column from the 'students' table
        op.drop_column('students', 'email')
        logger.info("Removed 'email' column from 'students' table successfully.")

    except Exception as e:
        logger.error("Error removing 'email' column from 'students' table: %s", e)
        raise
```