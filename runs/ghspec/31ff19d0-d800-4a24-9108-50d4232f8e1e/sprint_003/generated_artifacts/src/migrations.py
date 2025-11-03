```python
# src/migrations.py

from flask_migrate import Migrate, upgrade as FlaskUpgrade, downgrade as FlaskDowngrade
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

# Initialize the database
db = SQLAlchemy()

# Migration commands
def upgrade():
    """Run the upgrade operation to create the 'course' table."""
    try:
        # Create the 'course' table with necessary fields
        op.create_table(
            'course',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True, nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('level', sa.String(), nullable=False)
        )
    except SQLAlchemyError as e:
        # Handle any potential errors during table creation
        print(f"An error occurred while creating the course table: {e}")

def downgrade():
    """Run the downgrade operation to drop the 'course' table if it exists."""
    try:
        op.drop_table('course')
    except SQLAlchemyError as e:
        # Handle any potential errors during table deletion
        print(f"An error occurred while dropping the course table: {e}")

def migrate_db():
    """Run database migrations without data loss."""
    try:
        FlaskUpgrade()
        print("Database migration completed successfully.")
    except SQLAlchemyError as e:
        # Log error that occurred during migration
        print(f"An error occurred during database migration: {e}")

# Bind the application for migrations
def bind_app(app):
    """Bind the Flask app to the database for migrations."""
    Migrate(app, db)
```