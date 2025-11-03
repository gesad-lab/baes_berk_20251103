```python
# database/__init__.py

from alembic import op
import sqlalchemy as sa
from app import db

# Function to run migrations on application startup
def run_migrations():
    """Run all pending database migrations during application startup."""
    from alembic.config import Config
    from alembic import command

    # Load Alembic configuration
    alembic_cfg = Config('alembic.ini')  # Ensure this file exists and is configured properly
    alembic_cfg.set_main_option('script_location', 'migrations')  # Path to migrations folder

    # Run the upgrade command to apply all migrations
    with op.get_context().autocommit_block():
        command.upgrade(alembic_cfg, 'head')

# Add a function that initializes the database and runs migrations
def initialize_database():
    """Initialize the database and run migrations at startup."""
    with db.app.app_context():  # Create a database session
        run_migrations()
        # Perform any other startup necessary initialization if needed
```
