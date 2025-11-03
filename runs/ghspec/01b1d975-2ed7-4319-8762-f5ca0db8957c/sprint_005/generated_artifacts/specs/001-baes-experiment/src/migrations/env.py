```python
# migrations/env.py

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from logging import getLogger
import logging

# Add your model's metadata here
from src.models import db

logger = getLogger('alembic.env')

config = context.config

# Set up logging
logging.basicConfig()
logger.setLevel(logging.INFO)

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=db.metadata,
            process_bind_param=True,
            include_schemas=True,
        )

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=config.get_main_option('sqlalchemy.url'),
        target_metadata=db.metadata,
        literal_binds=True,
        dialect_opts={" paramstyle": "named"},
        include_schemas=True,
    )

    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# Migration script for 'teachers' table
def upgrade():
    """Create the teachers table."""
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    """Drop the teachers table."""
    op.drop_table('teachers')
```